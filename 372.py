s = input().strip()
zeros_sequences = s.split('1')
max_len = max(len(seq) for seq in zeros_sequences)
print(max_len)