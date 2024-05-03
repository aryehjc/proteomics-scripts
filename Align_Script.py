#!/usr/bin/env python3
import sys
import subprocess as sp
import os

reference_genome=[
'AP018436_1_MABS.fasta',
        ]
    

all_assemblies=[]
f=open("assemblies.txt").readlines()
for i in f:
    all_assemblies.append(i.strip())

# if theres a slash after -p %s/ below its weird for some reason
       
for n,rg in enumerate(reference_genome):
    refid=rg.split("_")[0]
    for m,strains in enumerate(all_assemblies):
        if rg != strains:
            strains_id=strains.split('.')[0]
            sp.call('dnadiff FASTA/%s FASTA/%s -p %s_%s_%s'%(rg,strains,refid,refid,strains_id),shell=True)
