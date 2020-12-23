import argparse
import codecs
from PhishCanary import english_confusables
from PhishCanary.__init__ import __version__
import os
import dns.resolver
import tldextract


def is_ascii(name):
    res = True
    for i in name:
        if ord(i) >= 128:
            res = False
            break
    return res


def calc_min_distance(input_str, substr):
    dp_table = []
    for i in range(len(substr) + 1):
        dp_table.append([0] * (len(input_str) + 1))

    for i in range(1, len(substr) + 1):
        dp_table[i][0] = i

    for i in range(1, len(substr) + 1):
        for j in range(1, len(input_str) + 1):

            if substr[i - 1] != input_str[j - 1]:
                min_val = min([dp_table[i][j - 1], dp_table[i - 1][j - 1], dp_table[i - 1][j]])
                min_val += 1
            else:
                min_val = dp_table[i - 1][j - 1]

            dp_table[i][j] = min_val

    return min(dp_table[-1][:])


def read_lines(file):
    for line in file:
        line = line.strip().lower()
        if not line.startswith("#"):
            yield line


def get_domains(target_file_path):
    result = set()

    with(open(target_file_path, "r")) as target_file:
        for line in read_lines(target_file):
            result.add(line)

    return result


def get_authoritative_dns_servers(domains):
    result = {}
    for domain in domains:
        if domain not in result:
            answers = dns.resolver.query(domain, 'NS')
            for server in answers:
                parsed_server = tldextract.extract(server.to_text())
                authoritative_server = parsed_server.registered_domain
                if authoritative_server not in result:
                    result[authoritative_server] = set()
                result[authoritative_server].add(domain)

    return result


def find_last_ln(file, index):
    step_size = 1000
    read_index = index
    found = False
    location = -1
    while not found:
        read_index = read_index - step_size
        file.seek(read_index, 0)
        read_buffer = file.read(step_size)
        for i in range(len(read_buffer) - 1, -1, -1):
            if read_buffer[i] == '\n':
                location = read_index + i
                found = True
                break
    return location + 1


def jump_to_records(file, startswith):
    file.seek(0, 2)
    start = 0
    end = file.tell()
    while start < end:
        middle = file.seek(start + (end - start) / 2, 0)
        middle = find_last_ln(file, middle)
        file.seek(middle, 0)
        current_line = file.readline()

        if (end - start) < 1000:
            break
        elif current_line < startswith:
            start = middle
        else:
            end = middle

    start = find_last_ln(file, start)
    file.seek(start, 0)


def dump_punycode_domains(zone_file_path, dump_file_path, is_sorted=True):
    with open(zone_file_path, "r") as zone_file:
        if is_sorted:
            jump_to_records(zone_file, "xn--")
        with open(dump_file_path, "w", encoding='utf-8') as dump_file:
            counter = 0
            seen = set()
            for line in zone_file:
                counter += 1
                if line.startswith('xn--'):
                    domain_str = line.split()[0].rstrip('.')
                    last_dot_index = domain_str.rfind('.')
                    if last_dot_index > 0:
                        puny = domain_str[4:last_dot_index]
                    else:
                        puny = domain_str[4:]
                    if puny not in seen:
                        seen.add(puny)
                        try:
                            unicode = codecs.getdecoder('punycode')(puny)[0]
                            ascii_rep = english_confusables.convert_to_ascii(unicode)

                            if ascii_rep != unicode and is_ascii(ascii_rep):
                                ascii_rep = ascii_rep.upper()

                                dump_file.write("{},{},{},{}".format(ascii_rep, puny, unicode, line))
                        except UnicodeError:
                            pass


def process(args):
    file_path = args.zonefile
    file_path_output = file_path + ".dmp"

    if os.path.isfile(file_path_output) is False:
        dump_punycode_domains(file_path, file_path_output, is_sorted=args.sorted)

    target_domains = get_domains(args.targets)
    authoritative_dns = get_authoritative_dns_servers(target_domains)
    trusted_dns = get_domains(os.path.join("configs", "trusted_nameservers.conf"))

    ascii_reps = {}
    file = open(file_path_output, "r", encoding="utf-8")

    for i in file:
        ascii_rep, *rest = (x.strip() for x in i.split(','))
        name_server_str = rest[-1].split()[-1]
        name_server = tldextract.extract(name_server_str).registered_domain
        ascii_rep = ascii_rep.lower()
        if ascii_rep not in ascii_reps:
            ascii_reps[ascii_rep] = []
        ascii_reps[ascii_rep].append((rest[0], rest[1], rest[2], name_server))

    potential_phish = {}
    
    print('target,ascii,unicode,punycode,NS record')
    for target_domain in target_domains:
        target_domain = tldextract.extract(target_domain).domain

        for domain in ascii_reps:
            min_dist = calc_min_distance(domain, target_domain)
            rec = ascii_reps[domain][-1]
            if min_dist <= 1 and \
                    rec[-1] not in authoritative_dns and \
                    rec[-1] not in trusted_dns:
                print('{},{},{},{}'.format(
                    target_domain,
                    domain,
                    rec[1],
                    rec[2]
                ))

    for i in potential_phish:
        print("{}:{}".format(i, potential_phish[i]))


def get_logo():
    return """                                                         
      ___         ___                       ___           ___                     
     /\  \       /\  \                     /\__\         /\  \                    
    /::\  \      \:\  \       ___         /:/ _/_        \:\  \                   
   /:/\:\__\      \:\  \     /\__\       /:/ /\  \        \:\  \                  
  /:/ /:/  /  ___ /::\  \   /:/__/      /:/ /::\  \   ___ /::\  \                 
 /:/_/:/  /  /\  /:/\:\__\ /::\  \     /:/_/:/\:\__\ /\  /:/\:\__\                
 \:\/:/  /   \:\/:/  \/__/ \/\:\  \__  \:\/:/ /:/  / \:\/:/  \/__/                
  \::/__/     \::/__/       ~~\:\/\__\  \::/ /:/  /   \::/__/                     
   \:\  \      \:\  \          \::/  /   \/_/:/  /     \:\  \                     
    \:\__\      \:\__\         /:/  /      /:/  /       \:\__\                    
     \/__/       \/__/         \/__/       \/__/         \/__/                    
      ___           ___           ___           ___           ___                 
     /\__\         /\  \         /\  \         /\  \         /\  \                
    /:/  /        /::\  \        \:\  \       /::\  \       /::\  \         ___   
   /:/  /        /:/\:\  \        \:\  \     /:/\:\  \     /:/\:\__\       /|  |  
  /:/  /  ___   /:/ /::\  \   _____\:\  \   /:/ /::\  \   /:/ /:/  /      |:|  |  
 /:/__/  /\__\ /:/_/:/\:\__\ /::::::::\__\ /:/_/:/\:\__\ /:/_/:/__/___    |:|  |  
 \:\  \ /:/  / \:\/:/  \/__/ \:\~~\~~\/__/ \:\/:/  \/__/ \:\/:::::/  /  __|:|__|  
  \:\  /:/  /   \::/__/       \:\  \        \::/__/       \::/~~/~~~~  /::::\  \  
   \:\/:/  /     \:\  \        \:\  \        \:\  \        \:\~~\      ~~~~\:\  \ 
    \::/  /       \:\__\        \:\__\        \:\__\        \:\__\          \:\__\\
     \/__/         \/__/         \/__/         \/__/         \/__/           \/__/    
                                                        
    """


def main():
    print(get_logo())
    print('PhishCanary(v{}) - {}\n'.format(__version__,
                                           "https://github.com/DissectMalware/PhishCanary"))

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("-f", "--zonefile", type=str, action='store',
                            help="Specify a TLD zone file path", metavar=('FILE_PATH'))
    arg_parser.add_argument("-t", "--targets", type=str, action='store',
                            help="Specify a file containing target domain names", metavar=('FILE_PATH'))
    arg_parser.add_argument("-s", "--sorted", default=True, action='store_true',
                            help="Determine whether the lines in the input are sorted")

    args = arg_parser.parse_args()

    complete = True

    if not args.zonefile:
        print('Error: --zonefile is missing\n')
        complete = False
    if not args.targets:
        print('Error: --targets is missing\n')
        complete = False

    if not complete:
        arg_parser.print_help()
    else:
        process(args)


if __name__ == '__main__':
    main()
