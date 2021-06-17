# -*- coding: utf-8 -*-
"""
Created on Tue Jun  10 11:18:27 2021

@author: DostS
"""

#import helping librarires
import json
import csv
import requests
import ast

# upload ActivityNet-Entity-Data-Train and Validation set json file
with open('../dataset/ActivityNet-Entity/anet_entities_cleaned_class_thresh50_trainval.json', 'r') as myfile:
    data=myfile.read()
anet_ground_anno_train = json.loads(data)

#take the annotation part
annotation = anet_ground_anno_train['annotations']

def get_entity_linking(entity):
"""
This funciton take a textual and process via Falcon for entity linking to DBpedia and Wikidata
"""

    headers = {'Content-type': 'application/json',}
    data = '{"text":"'+entity+'"}'
    response = requests.post('https://labs.tib.eu/falcon/falcon2/api?mode=short&db=1', headers=headers, data=data)

    # content part from requests
    linked_data_cont = response.content
    mydata = ast.literal_eval(linked_data_cont.decode("UTF-8"))

    linked_entity = []
    for key in mydata:
        for value in mydata[key]:
            # print(value[0])
            linked_entity.append(value[0])

    return linked_entity


count = 0
count_process_class = 0


with open('D:/TIB/VGD_KR/KR/csv_with_linked_data_v1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Doc_ID','Segment_ID','process_Idx','process_Class','DBpedia','Wikidata','process_bnd_Box','ybr','ytl','xbr','xtl','frame_Ind','Crowds'])

    for doc_id, doc_data in annotation.items():
        doc_segment =  doc_data['segments']
        for seg_id, seg_data in doc_segment.items():

            token = seg_data['tokens']
            process_Idx = seg_data['process_idx']
            process_Class = seg_data['process_clss']
            process_bnd_Box = seg_data['process_bnd_box']
            frame_Ind = seg_data['frame_ind']
            Crowds =  seg_data['crowds']

            #Make proper Seg_ID
            Seg_ID = doc_id+'/'+seg_id


            for i in range(len(process_Idx)):
                count_process_class+=1

                for j in range(len(process_Idx[i])):
                    count_process_class+=1
                    #process_Idx
                    Process_Idx = Seg_ID+'/'+str(process_Idx[i][j])
                    linked_entities = get_entity_linking(process_Class[i][j])

                    dbpedia = linked_entities[0]
                    wikidata = linked_entities[1]

                    #clean wikidata URI
                    wikidata_clean = wikidata[1:-1]

                    # print(process_Class[i][j],dbpedia,wikidata_clean)
                    writer.writerow([doc_id,Seg_ID,Process_Idx,process_Class[i][j],dbpedia,wikidata_clean,process_bnd_Box[i],process_bnd_Box[i][0],process_bnd_Box[i][1],process_bnd_Box[i][2],process_bnd_Box[i][3],frame_Ind[i],Crowds[i]])

        count+=1
        print('Document no->',count,count_process_class)
        # if count>=10:
            # break
