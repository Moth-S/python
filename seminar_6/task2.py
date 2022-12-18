# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;

def Find_parentheses(s):
    for i in range(s.count('(')):
        s1 = ''
        if '(' in s:
            s1 = s[s.index('(')+1:s.index(')')]
            s1 = Solution(Find_num(s1))
            s = s.replace(s[s.index('('):s.index(')')+1], str(s1))
        if '--' in s:
            s = s.replace('--', '+')
    return s


def Find_num(s):
    s += ' '
    s1 = ''
    rez_s = []
    for i in range(len(s)):
        if s[i] in '0123456789':
            s1 += s[i]
        else:
            rez_s.append(int(s1))
            s1 = ''
            rez_s.append(s[i])
    rez_s.pop(-1)
    # print(rez_s)
    return rez_s


def Solution(s):

    for j in range(1, len(s)-1):
        if s[j] == '*':
            s[j+1] = s[j-1]*s[j+1]
            s[j-1], s[j] = '?', '?'
        elif s[j] == "/":
            s[j+1] = s[j-1]/s[j+1]
            s[j-1], s[j] = '?', '?'
        elif s[j] == "-":
            s[j+1] *= (-1)
            s[j] = '?'
        elif s[j] == "+":
            s[j] = '?'
    while '?' in s:
        s.pop(s.index('?'))

    # print(sum(s))
    return (sum(s))


strng = input("Введите выражение: ")
s1 = Find_num(Find_parentheses(strng))
print(Solution(s1))
