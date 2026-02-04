# CTF Notes

## Accounts

- [picoCTF](https://play.picoctf.org/users/dhalgren)

### Week of Feb 1 26

disk analyis, basics

- picoCTF 85: grep, egrep; wget for downloading files, 'file' for explaining file based on contents, 'find', tree -I, -a for all
- picoCTF 301,300 - disk analysis, analyzing disk image partition with mmls, fls, icat, etc.
  - Media: media layer tools prepend with 'mm', mmls gives partition table. Media is lowest level
  - Block: second lowest level, block tools prepend with blk, blkcat outputs contents of a single block
  - Inode: bookkeeping layer, table of contents. tools prepend with i, icat outputs single file based on inode number
  - filename: tools prepend with f, fls lists files on image starting at root; looks similar to typical shell
- pico137, 285

packet analysis

- pico 286: wireshark, packets. filter with !arp, discards arp. ARP - Address Resolution Protocol, connects a hardware address to an IP
  - first 3 are tcp handshake
  - [PSH] flag signifies there is data for the application in the packet
  - TCP handshake is 3-way, identified by the flags
    - SYN from host A; SYN, ACK from host B; ACK from host A; synchronization, acknowledgement
  - strategy to filter as many packets as possible and then look for oddities
  - flag can span multiple packets

network layers

- application layer: responsible for handling data traffic, http
- transport layer: responsible for providing several connections on same host, defines functionalities for reliable transport, eg TCP transport control protocol makes sure failed packets are re-sent. HTTP from the app layer runs on top of TCP. When reliability not a concern, UDP user datagram protocol is used, used in voice communication, faster than tcp, assigns port to each connection
- network layer: provides devices with an address in the network, IP internet protocol address
- data link layer: provides communication between devices that are connected directly. eg ethernet or wifi. Physical addresses: mac addresses assigned to hardware of the network card when it is manufactured, does not change like IP.
- physical layer: handles electric pulses on the wire that represent bits
