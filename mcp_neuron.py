from random import *

# Created by Rebecca Dsouza on 26-07-19


def and_gate(arg1, arg2):
	wt = [1, 1]
	threshold = 2

	if wt[0]*arg1 + wt[1]*arg2 >= threshold: return 1
	else: return 0


def not_gate(arg1):
	wt = [-1]
	threshold = 0

	if wt[0]*arg1 >= threshold: return 1
	else: return 0


def or_gate(arg1, arg2):
	wt = [1, 1]
	threshold = 1

	if wt[0] * arg1 + wt[1] * arg2 >= threshold: return 1
	else: return 0


def xor_gate(arg1, arg2):
	return or_gate(and_gate(arg1, not_gate(arg2)), and_gate(not_gate(arg1), arg2))


def half_adder(arg1, arg2):
	add = xor_gate(arg1, arg2)
	carry = and_gate(arg1, arg2)
	return add, carry


for ip in [[0, 0], [0, 1], [1, 0], [1, 1]]:
	print('{0} AND {1} = {2}'.format(ip[0], ip[1], and_gate(ip[0], ip[1])))
	print('{0} OR {1} = {2}'.format(ip[0], ip[1], or_gate(ip[0], ip[1])))
	ans = half_adder(ip[0], ip[1])
	print('{0} ADD {1} : SUM = {2} CARRY = {3}'.format(ip[0], ip[1], ans[0], ans[1]))
	print('-'*30)

for ip in [randrange(-10, 5) for _ in range(10)][::2][:3]:
	print('NOT {0} = {1}'.format(ip, not_gate(ip)))

print('-'*30)
