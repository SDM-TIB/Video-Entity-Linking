# ActivityNet-EKG

### Introduction
This repository consists of scripts, dataset files, unified schema, and rml files for generating ActivityNet-EKG knowledge graph. Video-Textual-Knowledge-Entity-Linking, known as ActivityNet-EKG contains video short clips and is associated with descriptions (captions) in which visual objects and textual entities are aligned with entity mentions in their corresponding classes (types) in knowledge bases called DBpedia and Wikidata. The ActivityNet-EKG knowledge graph can open new research directions and can used to solve the problems of multimedia processing, indexing, and retrieval tasks, e.g., information extraction from [video-text](https://www.sciencedirect.com/science/article/pii/S0031320303004175), [video questions answering](https://arxiv.org/abs/1809.01696), [video captioning](https://www.ics.uci.edu/~dechter/courses/ics-295/fall-2019/presentations/Porhemmat.pdf), and [video dialogue systems](https://arxiv.org/abs/1907.01166).

The below Figure shows how the vision and language parts come to form three segments with captions describing the video contents. The knowledge base (KB) part represents the recognized and linked entities in the same colors with corresponding classes (types) in the KB and represents their actual DBpedia linked in the table.

![EKG_fig1](https://github.com/SDM-TIB/Video-Entity-Linking/assets/25593410/d560dc1f-15ba-4d6f-8fb0-57517491d681)

### VIDEO-TEXTUAL-KNOWLEDGE-ENTITY-LINKING-(VITEL)
We proposed a novel task called ViTEL (Video-Textual-Knowledge-Entity-Linking), in which the document is composed of textual data, visual data (in the form of video frames), and a knowledge base. The ViTEL task is trying to recognize and link maximum portions of visual and textual parts with the corresponding entity mentions (or classes) in the knowledge base, or linking them to new entities, extending the A-box of knowledge base with its type assertion(s). The ViTEL closed the loops between vision (i.e., videos), language (texts), and semantics (background knowledge) modalities.

###  Framework for ActivityNet-EKG development
The below Figure shows the general architecture of the framework which is also used for the development of ActivityNet-EKG knowledge graph. The input to the framework can be visual data (e.g. images or videos), textual data, and annotated data, (ii) the textual part can be processed by entity recognition and linking tasks/tool, (iii) the annotation of visual data has been used for the visual part or a visual object detector can be used in this part. The descriptive mapping rules (e.g. RML) will map the heterogeneous data into RDF triples to generate a knowledge graph. The resultant knowledge graph can be used in the graph database (e.g. GraphDB).


![EKG_fig2](https://github.com/SDM-TIB/Video-Entity-Linking/assets/25593410/7a618da5-7004-440d-82bf-3c1697b90a72)

### Statistics of ActivityNet-EKG and ActivityNet-EKG*
Statistics of the developed ActivityNet-EKG* (AN-EKG*), and ActivityNet-EKG (AN-EKG) are shown in the below table.

![EKG_tab1](https://github.com/SDM-TIB/Video-Entity-Linking/assets/25593410/5bf2cdcb-2999-427a-b827-29072d282fec)


###  Single entry of the ActivityNet-EKG Knowledge-Graph
A single entry of the ActivityNet-EKG knowledge graph is represented below. A video segment consists of three video frames and a textual caption describing the visual part. Figure b shows the SPARQL query for extracting RDF triples for a document with ID:v_QOlSCBRmfWY. A small RDF-based knowledge graph for a single entry is shown in green (the resource information), and blue and yellow triples (textual and visual portions).

![EKG_fig4](https://github.com/SDM-TIB/Video-Entity-Linking/assets/25593410/c29c15cb-05de-434b-85c6-e8627a88717a)

### Cite
If you find HyAI helpful in your work please cite the paper:
```
Shahi Dost, Maria-Esther Vidal, Hanan Begali, Enrique Iglesias, Ahmad Sakor. 2023.
Knowledge Capturing from Multimodal Video-Textual Knowledge-Entity Linking (KCAP’2023)[https://www.k-cap.org/2023/]
```

### License
The codes and source files are licensed under [MIT License](https://github.com/SDM-TIB/Video-Entity-Linking/blob/main/LICENSE).

### Authors
