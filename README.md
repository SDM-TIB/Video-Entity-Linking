# ActivityNet-EKG

### Introduction
This repository consists of scripts, datasets, unified schema, and RML files for generating ActivityNet-EKG and ActivityNet-EKG* knowledge graphs. ActivityNet-EKG contains short clips of video and their descriptions (captions) in which visual objects and textual entities are aligned with entity mentions in their corresponding classes (types) in knowledge bases called [DBpedia](https://www.dbpedia.org/) and [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page). The ActivityNet-EKG knowledge graphs can open new research directions and can used to solve the problems of multimedia processing, indexing, and retrieval tasks, e.g., information extraction from [video-text](https://www.sciencedirect.com/science/article/pii/S0031320303004175), [video questions answering](https://arxiv.org/abs/1809.01696), [video captioning](https://www.ics.uci.edu/~dechter/courses/ics-295/fall-2019/presentations/Porhemmat.pdf), and [video dialogue systems](https://arxiv.org/abs/1907.01166).

The below Figure shows how the vision and language parts come into play to form three segments with captions describing the video contents. The knowledge base (KB) part represents the recognized and linked entities in the same colors with corresponding classes (types) in the KB and represents their actual DBpedia linked in the table.

![EKG_fig1](https://github.com/SDM-TIB/Video-Entity-Linking/assets/25593410/d560dc1f-15ba-4d6f-8fb0-57517491d681)

### VIDEO-TEXTUAL-KNOWLEDGE-ENTITY-LINKING-(ViTEL)
We proposed a novel task called ViTEL (Video-Textual-Knowledge-Entity-Linking), in which the document is composed of textual data, visual data (in the form of video frames), and a knowledge base. The ViTEL task is trying to recognize and link maximum portions of visual and textual parts with the corresponding entity mentions (or classes) in the knowledge base, or linking them to new entities, extending the A-box of knowledge base with its type assertion(s). ActivityNet-EKG and ActivityNet-EKG* knowledge graphs can be used for the design, training and evaluation of algorithms solving the task of ViTEL. The ViTEL closed the loops between vision (i.e., videos), language (texts), and semantics (background knowledge) modalities.

### Framework for ActivityNet-EKG and ActivityNet-EKG* development
The below Figure shows the architecture of the framework which is also used for the development of ActivityNet-EKG and ActivityNet-EKG* knowledge graphs. The input to the framework is visual data (e.g. images or videos), textual data, and annotated data, (ii) the textual part is processed by entity recognition and linking tasks/tool, (iii) the annotation of visual data has been used for the visual part or a visual object detector can be used in this part. The descriptive mapping rules (e.g. RML) have mapped the heterogeneous data into RDF triples to generate knowledge graph. The resultant knowledge graph can be saved in the graph database (e.g. GraphDB).


![EKG_fig2](https://github.com/SDM-TIB/Video-Entity-Linking/assets/25593410/7a618da5-7004-440d-82bf-3c1697b90a72)

### Statistics of ActivityNet-EKG and ActivityNet-EKG*
Statistics of the developed ActivityNet-EKG (AN-EKG) and ActivityNet-EKG* (AN-EKG*) are shown in the below table.

![EKG_tab1](https://github.com/SDM-TIB/Video-Entity-Linking/assets/25593410/5bf2cdcb-2999-427a-b827-29072d282fec)


###  Example from the ActivityNet-EKG Knowledge-Graph
A single entry of the ActivityNet-EKG knowledge graph is represented below in details. A video segment consists of three video frames (each frame has one bounding box) and a textual caption describing the visual part. Figure b shows the SPARQL query for extracting RDF triples for a document with ID:v_QOlSCBRmfWY. A small RDF-based knowledge graph for this entry is shown in green (the resource information), and blue and yellow RDF triples (textual and visual portions).

![EKG_fig4](https://github.com/SDM-TIB/Video-Entity-Linking/assets/25593410/c29c15cb-05de-434b-85c6-e8627a88717a)

### Cite
If you find ActivityNet-EKG, ActivityNet-EKG* and ViTEL helpful in your work please cite the paper:
```
Shahi Dost, Maria-Esther Vidal, Enrique Iglesias, Ahmad Sakor. 2023.
Knowledge Capturing from Multimodal Video-Textual Knowledge-Entity Linking (KCAP’2023)[https://www.k-cap.org/2023/]
```

### License
The source codes and files are licensed under [MIT License](https://github.com/SDM-TIB/Video-Entity-Linking/blob/main/LICENSE).

### Contact
If you have any query regarding ActivityNet-EKG, ActivityNet-EKG*, ViTEL, source files, or want to contribute to this work, please contact on shahi.dost[at]tib.eu.
