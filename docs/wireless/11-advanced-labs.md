# Advanced Wireless Labs

## Secure Communications with HTTPS

In our documentation we frequently refer to secure communications as using a "Secure Sockets Layer".  Although the term "SSL" is common, we are actually using a protocol called Transport Layer Security (TLS).

TLS replaces SSL.  It is an Internet Engineering Task Force (IETF) standard protocol that provides authentication, privacy and data integrity between two communicating computer applications.

!!! Note
    The standard Python [request library](https://www.w3schools.com/python/module_requests.asp) does not yet support HTTPS on urequest on the Pico W.  This is because there are additional tools that require us to use keys and certificates to validate data on an encrypted SSL stream.

See the [MicroPython SSL/TLS Library](https://docs.micropython.org/en/latest/library/ssl.html)

## Testing SSL/TLS on Standard Python

```python
import socket
import ssl

hostname = 'www.python.org'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
```

returns: TLSv1.3

This tells you that the standard Python socket libraries use the TLS v1.3 protocol.

## Performance Monitoring with uiperf3

[iperf3](https://iperf.fr/iperf-doc.php) is a standard Python program for internet performance testing.  For micropython, we have our own stripped down version called uiperf3.

IPerf3 uses a client-server testing model and measures networking performance between two system using various protocoos such as

* UDP - User Datagram Protocol
* TCP - Transmission Control  Protocol
* Streaming

It can also be used to measure total wireless throughput.

## UPIP Install

```py
upip.install("uiperf3")
```

## Testing Client Performance
```python
import uiperf3
 uiperf3.client('MY_IP_ADDRESS')
```



