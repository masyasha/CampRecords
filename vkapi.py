# -*-coding: UTF-8-*-

import datetime
from time import sleep
import vk

ids = [[{171834392: 'False', 317000045: 'False', 279659978: 'False', 235760861: 'False', 102636182: 'False', 
		255828887: 'False', 332943714: 'False', 251601110: 'False'}], [{147623823: 'False', 192282006: 'False', 
		339375663: 'False', 169907505: 'False', 215186179: 'False', 147416477: 'False', 94955287: 'False',
		199397602: 'False', 98405942: 'False', 181816944: 'False'}], [{201053498: 'False', 183644476: 'False', 
		335869032: 'False', 89813996: 'False', 214004729: 'False', 78113067: 'False', 149584785: 'False', 
		184918216: 'False', 51758427: 'False', 1286959: 'False'}]]

def get_status(current_status, vk_api, id, house):
	user_info = vk_api.users.get(user_id=id, fields='online')
	f_name = str(user_info[0]['first_name'])
	l_name = str(user_info[0]['last_name'])
	if (current_status == 'False') and (user_info[0]['online']): 
	    print(f_name, l_name, 'is online.')
	    return 'True'
	if (current_status == 'True') and (not user_info[0]['online']):
		print(f_name, l_name, 'is now offline.')
		return 'False'
	return current_status


session = vk.Session()
vk_api = vk.API(session)
while(True):
	for i in range(len(ids)):
	    for id in ids[i][0].keys():
	    	current_status = ids[i][0][id]
	    	current_status = get_status(current_status, vk_api, id, i)
	    	ids[i][0][id] = current_status
	    	sleep(0.5)


# Идеи на будущее:

#	1. Интегрировать приложение с google forms, которые заполняет каждый участник
#	2. Автоматизировать процесс получения всех ID
#	3. Выводить имена и фамилии тех, кто онлайн после отбоя, а также номер, в котором они живут
#	4. Сделать аудиосопровождение
#	5. Посылать поток данных arduino дистанционно, безпроводным способом
