# PhishCanary
Given a TLD zone file, PhishCanary extracts International Domain Names (IDNs) that are homoglyphs of specified target domain names.

PhishCanary filters out the IDNs created by the target domain names' authoritative nameservers or by trusted domain names.


# Installing PhishCanary

1. Installing from Repository

```
pip install -U https://github.com/DissectMalware/PhishCanary/archive/master.zip
```

# Running PhishCanary
To extracts suspicious IDNs from a zone file

```
phishcanary --zonefile com.zone  --targets target-domains.txt

phishcanary -f com.zone  -t target-domains.txt
```

Where target-domains.txt contain a list of domain names that we are interested in:

```
target-domains.txt:
microsoft.com
twitter.com
instagram.com
yahoo.com
youtube.com
facebook.com
```

Sample ouput can be found https://pastebin.com/waYKKd1H


# Command Line

```

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
    \::/  /       \:\__\        \:\__\        \:\__\        \:\__\          \:\__\
     \/__/         \/__/         \/__/         \/__/         \/__/           \/__/


PhishCanary(v0.1.0) - https://github.com/DissectMalware/PhishCanary

usage: extractor.py [-h] [-f FILE_PATH] [-t FILE_PATH] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_PATH, --zonefile FILE_PATH
                        Specify a TLD zone file path
  -t FILE_PATH, --targets FILE_PATH
                        Specify a file containing target domain names
  -s, --sorted          Determine whether the lines in the input are sorted

```

# Requirements

It relies on the following libraries: dnspython and tldextract


# How to Contribute
If you found a bug or would like to suggest an improvement, please create a new issue on the [issues page](https://github.com/DissectMalware/PhishCanary/issues).

Feel free to contribute to the project forking the project and submitting a pull request.

You can reach [me (@DissectMlaware) on Twitter](https://twitter.com/DissectMalware) via a direct message.

