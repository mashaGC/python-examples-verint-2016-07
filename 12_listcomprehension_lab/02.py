_author_ = 'mariag'

abc1 = [chr(i) for i in range(97,123)]

comb = sorted(set([a+b+c for a in abc1 for b in abc1 for c in abc1]))

print comb