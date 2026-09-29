# rsocx

SUMMARY:

The rsocx repository provides a high-performance Socks5 proxy server implemented in Rust using the Async-std framework. It supports both bind and reverse modes, with no use of unsafe code or multiple executables. The software is compatible across Linux, Windows, macOS, and BSD platforms. 

Key features include:
- Bind mode: Listening on port 1080 for standard Socks5 connections.
- Reverse mode: Accepting slave connections on a specified port (e.g., 8000) and establishing reverse connections to the master server.

Performance benchmarks show rsocx achieving a throughput of approximately 12.90 seconds for 1,000 requests via Proxychains4 to a Tornado Python service running on Ubuntu 20.04 in a LAN environment. 

Comparison with other Socks5 implementations (merino, go-socks5, simple-socks, asio5, esocks) indicates rsocx's competitive performance, though it lacks support for SOCKS5 authentication methods and some command features like `BIND` and `ASSOCIATE`.

KEYWORDS:
rsocx, Socks5 proxy, Rust, Async-std, bind mode, reverse mode, performance benchmark, Proxychains4, Tornado Python, LAN environment, comparison with merino, go-socks5, simple-socks, asio5, esocks.
