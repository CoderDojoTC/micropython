# Advanced Wireless Labs

## Secure Sommunications with HTTPS

TBD

!!! Note
    The standard Python [request library](https://www.w3schools.com/python/module_requests.asp) does not yet support HTTPS on urequest on the Pico W.  This is because there are additional tools that require us to use keys and certificates to validate data on an encrypted SSL stream.

See the [MicroPython SSL/TLS Library](https://docs.micropython.org/en/latest/library/ssl.html)

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



