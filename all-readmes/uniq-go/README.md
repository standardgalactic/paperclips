# No Hassle Unique Identifiers in Go

[![GoDoc](https://godoc.org/github.com/rwxrob/uniq-go?status.svg)](https://godoc.org/github.com/rwxrob/uniq-go)
[![Go Report
Card](https://goreportcard.com/badge/github.com/rwxrob/uniq-go)](https://goreportcard.com/report/github.com/rwxrob/uniq-go)
[![Coverage](https://gocover.io/_badge/github.com/rwxrob/uniq-go)](https://gocover.io/github.com/rwxrob/uniq-go)

`go get github.com/rwxrob/uniq-go`

Package `uniq` is a utility package that provides common random unique identifiers in UUID, Base32, and n*2 random hexadecimal characters.

    6c671957-2f39-4ce5-9f0e-e8d5ec53bfde (16 bytes, 36 chars, hex-)
    H6M0STKP0MTSU0493GERQDCSJ5BMF3VO     (20 bytes, 32 chars, base32)
    5b ...                               (n bytes, n*2 chars, hex)

When a simple random identifier is all that is needed `Base32()` provides a better alternative to `UUID()`. It takes less space (32 characters), is safe for use with all file systems including case insensitive ones, and provides additional randomness increased from 2^128 (UUID) to 2^160 (Base32).

This package includes the following convenience commands as well for use when integrating with shell scripts:

* `uuid`
* `uid32`
* `isosec`
* `epoch [SECONDS]`
* `randhex [COUNT]`
