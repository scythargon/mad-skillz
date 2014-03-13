from blessings import Terminal

t = Terminal()
print t.red('This is red.')
print t.bold_green_on_black('Bold green on black')

print '{t.green}You'.format(t=t)+t.normal+' just cleared a {t.bold}whole{t.red_on_black} line!'.format(t=t)
