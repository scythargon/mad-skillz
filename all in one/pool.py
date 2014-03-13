#! /usr/bin/env python
# -*- coding: utf-8 -*-

from blessings import Terminal
import urwid
from random import randint
from Aurwid import *
import thread,logging
from time import strftime,time,sleep
from twisted.internet import reactor
from twisted.internet.defer import Deferred, DeferredList
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent, HTTPConnectionPool
from twisted.web.http_headers import Headers
from twisted.internet.error import AlreadyCalled, AlreadyCancelled

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.CRITICAL, filename = u'mylog.log')

class BeginningPrinter(Protocol):
    def __init__(self,handler):
        self.handler=handler
    def dataReceived(self, received):
        self.handler(received)
    def connectionLost(self, reason):
        pass

class Site():
    def __init__(self,url,rest,wait,pool,md5=None,ind=None,name=None):
        self.url = url
        self.rest = rest
        self.wait = wait
        self.pool = pool
        self.md5 = md5
        self.ind = ind if ind else 0
        self.name = name if name else self.url
        self.last_ask = 0
        self.last_received = 0
        self.agent = Agent(reactor, pool=pool)
        self.deferred = None
        self.delayedCall = None
    def __request(self):
        self.deferred = self.agent.request(
            'GET',
            self.url,
            Headers({'User-Agent': ['Mozilla/5.0']})
        )
        self.last_ask=time()
    def again(self):
        logging.debug(strftime('%X')+'again')
        #print strftime('%X'),'again'
        try:
            self.deferred.cancel()
        except (AlreadyCalled, AlreadyCancelled) :
            pass
        try:
            self.delayedCall.reset(self.wait)
        except (AlreadyCalled, AlreadyCancelled) :
            self.delayedCall = reactor.callLater(self.wait, self.timeIsOff)

        self.__request()
        self.deferred.addCallback(self.gotRequest)
    def timeIsOff(self):
        #print strftime('%X'),'time is off'
        logging.debug(strftime('%X')+'time is off')
        self.again()
    def handleReceived(self, received):
        #print strftime('%X'),'received: ',received
        logging.debug(strftime('%X')+'received: '+received)
    def gotRequest(self, response):
        #print strftime('%X'),'gotRequest'
        logging.debug(strftime('%X')+'gotRequest')
        self.last_received=time()
        self.again()
        #print 'Response code:', response.code
        logging.debug('Response code:'+ str(response.code))
        response.deliverBody(BeginningPrinter(self.handleReceived))
    def startLive(self):
        #print strftime('%X'),'startLive'
        logging.debug(strftime('%X')+'startLive')
        self.__request()
        self.deferred.addCallback(self.gotRequest)
        self.delayedCall = reactor.callLater(self.wait, self.timeIsOff)
    def norm_time(self,t):
        if t==0:
            return '0s'
        now=time()
        seconds=int(now-t) if now>t else int(t-now)
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return "%d:%02d:%02d" % (h, m, s) if h!=0 else "%d:%02d" % (m, s) if m!=0 else "%ds" % (s)
    def report(self):
        return {'name':self.name,
                'wait':str(self.wait),
                'rest':str(self.rest),
                'last_ask':self.norm_time(self.last_ask),
                'last_received':self.norm_time(self.last_received),
                'when_next':self.norm_time(self.delayedCall.getTime())}

class ArRow (urwid.WidgetWrap):

    def __init__ (self, site):
        self.site = site
        self.build_row()
        self._w = AColumns(self.item)
        self.__super.__init__(self._w)
    def build_row(self):
        sr = self.site_report = self.site.report()
        w=3
        self.item = [
            ('fixed',10,urwid.AttrWrap(urwid.Text(sr['name']), 'body', 'focus')),
            ('fixed',w,urwid.AttrWrap(urwid.Text(sr['wait']), 'body', 'focus')),
            ('fixed',w,urwid.AttrWrap(urwid.Text(sr['rest']), 'body', 'focus')),
            ('fixed',w,urwid.AttrWrap(urwid.Text(sr['last_ask']), 'body', 'focus')),
            ('fixed',w,urwid.AttrWrap(urwid.Text(sr['last_received']), 'body', 'focus')),
            ('fixed',w,urwid.AttrWrap(urwid.Text(sr['when_next']), 'body', 'focus')),
        ]
    def refresh(self):
        self.build_row()
        self._w = AColumns(self.item)
        #self.__super.__init__(w)
        logging.critical(str(self.site_report))
    def selectable (self):
        return True

    def keypress(self, size, key):
        return key

palette = [
    ('body','dark cyan', '', 'standout','#0f6',''),
    ('mooo','dark cyan', '', 'standout','light blue',''),
    ('focus','dark red', '', 'standout','light red',''),
    ('head','light red', 'black'),
    ]

def keystroke (input):
    if input in ('q', 'Q'):
        raise urwid.ExitMainLoop()

pool = HTTPConnectionPool(reactor)
site1 = Site(url='http://wool/cgi-bin/wait.cgi',rest=3,wait=4,pool=pool,name='finam.ru')
site2 = Site(url='http://wool/cgi-bin/wait.cgi',rest=3,wait=4,pool=pool,name='fxclub::евро')


site1.startLive()
site2.startLive()

items=[ArRow(site1),ArRow(site2)]
listbox = urwid.ListBox(urwid.SimpleListWalker(items))
view = urwid.Frame(urwid.AttrWrap(listbox, 'body'))
tw = TwistedEventLoop()
loop = urwid.MainLoop(view, palette, unhandled_input=keystroke, event_loop=tw)
loop.screen.set_terminal_properties(colors=256)

"""def loop_run_cap(*a):
    loop.run()
def reactor_run_cap(*a):
    reactor.run(installSignalHandlers=0)
"""
def live_report(_loop,_data):
    for item in items:
        item.refresh()
    loop.set_alarm_in(2,live_report)
        
#thread.start_new(reactor_run_cap,(0,))
#thread.start_new(live_report,(0,))
loop.set_alarm_in(2,live_report)
loop.run()

