#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import msgpack

MAX_TOPICSIZE_SHOW = 3

topicid2word = list() 
username2userid = dict()
userid2username = dict()
userid2etc = dict()
DATAS_DIRPATH = str()

def init():
	global topicid2word, username2userid, userid2username, userid2etc
	f = open(DATAS_DIRPATH+'data_msgpack')
	aaa = msgpack.load(f)
	f.close()
	topicid2word = aaa['topicid2word']
	username2userid = aaa['username2userid']
	userid2username = aaa['userid2username']
	userid2etc = aaa['userid2etc']

def output(username):
	"""
	usernameを入力として、類似のusernameを出力する
	"""
	print '全登録ユーザ数:', len(userid2etc)
	userid = username2userid[username]
	tmp = userid2etc[userid]
	print '＜類似ユーザ（ツイート内容から自動推定）＞'
	for uid in tmp[0]:
		print userid2username[uid]
	print '\n＜トピック語＞'
	topic_count = 1
	for tid in tmp[1][:MAX_TOPICSIZE_SHOW]:
		print 'Top', topic_count
		tmp_int = 1
		for w in topicid2word[tid]:
			print w,
			if tmp_int%10==0: print ''
			tmp_int += 1
		print ''
		topic_count += 1

def show_help():
	print 'エラー： 引数が不正です'
	print 'argv[1]: DATAS_DIRPATH'
	print 'argv[2]: username'
	print 'argv[3]: 出力するトピック数（省略可。MAX150）'

if __name__ == '__main__':
	if len(sys.argv) < 3 or len(sys.argv) > 4:
		show_help()
		sys.exit()
	DATAS_DIRPATH = sys.argv[1]
	if len(sys.argv) == 4:
		MAX_TOPICSIZE_SHOW = int(sys.argv[3])
	init()
	output(sys.argv[2])
