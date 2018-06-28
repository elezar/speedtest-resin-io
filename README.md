# Speedtest on resin.io

This repository contains an application based on (speedtest-cli)[https://github.com/sivel/speedtest-cli] for deployment on (resin.io)[https://resin.io].

The application consists of two services, `speedtest` and `fluentd` to perform the speedtest and log processing respectively.

## Notes:
- The Docker runtime used on resin.io (`balena`) has disabled the `fluentd` log driver [https://github.com/resin-os/balena/pull/7/commits/fe4d45c5dcbaddff51aebfe584a68e8fb9f44449]
