ip_logs = [
    "10.0.0.1",
    "192.16.0.1",
    "10.0.0.2",
    "192.168.1.105",
    "172.16.0.1",
    "192.168.1.105"
]

suspicious_ip = "192.168.1.105"

count=0

for ip in ip_logs:
    if ip == suspicious_ip:
        count += 1

print("Suspicious IP:", suspicious_ip)
print("Number of attempts:", count)


if count >= 3:
    print("ALERT! Suspicious IP attempted access 3 or more times.")
else:
    print("No alert. Attempts are less than 3.")
