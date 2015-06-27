
import bacteria


bacteris_list = []
Proteus_mirabilis = bacteria.Bacteria("Proteus mirabilis",
                                               "virulent killer",
                                               "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Proteus_mirabilis_01.jpg/240px-Proteus_mirabilis_01.jpg",
                                                None, 'pro_mir_gen.txt')

# Genome is for e. coli's plasmid pE2348
Escherichia_coli = bacteria.Bacteria("Escherichia coli", "E. coli and related bacteria constitute about 0.1% of gut flora, and pathogenic strains of the bacterium cause disease.",
                                     "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/EscherichiaColi_NIAID.jpg/250px-EscherichiaColi_NIAID.jpg",
                                     None, 'e_coli_0127_H6_gen.txt')
                                     
# Genome of single Helicobacter chromosome
Helicobacter = bacteria.Bacteria("Helicobacter","A gram_negative bacterium that infects up to 50% of human gastrointestinal tracts",
                                  "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Helicobacter_sp_01.jpg/240px-Helicobacter_sp_01.jpg",
                                  'helicobacter_gen.txt', None)
                                  
Clostridium_botulinum = bacteria.Bacteria("Clostridium botulinum", "Produces botulinum neurotoxin which is the cause of foodborn botulism",
                                          "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Clostridium_botulinum_01.png/240px-Clostridium_botulinum_01.png",
                                          None, "clost_bot_gen.txt")

# Genome is Yersinia pestis plasmid pPCP1 Sanger Institute version which differs by 2 base pairs from NCBI database
Yersinia_pestis = bacteria.Bacteria("Yersinia pestis", "A gram_negative bacterium that infects animals and humans and is responsible for pneumonic, septicemic and bubonic plagues",
                                    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Yersinia_pestis.jpg/220px-Yersinia_pestis.jpg", None,
                                    "yer_pest_gen.txt")

Pectobacterium_carotovorum = bacteria.Bacteria("Pectobacterium carotovorum", "Pectobacterium carotovora cause soft-rot diseases of various plant hosts through degradation of the plant cell walls",
                                               "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Slime_flux_on_Camperdown_elm.png/220px-Slime_flux_on_Camperdown_elm.png",
                                               "pect_carot_gen.txt", None)



#proteus_mirabilis.get_photo()

#print Proteus_mirabilis.define_genome()[1]
print Helicobacter.define_genome()[1]
print Helicobacter.bac_description()
Helicobacter.get_photo()


##print Proteus_mirabilis.bac_description()
##
##print Escherichia_coli.define_genome()[1]
##print Escherichia_coli.bac_description()
##
print Helicobacter.define_genome()[1]
print Helicobacter.bac_description()
##
##print Clostridium_botulinum.define_genome()[1]
##print Clostridium_botulinum.bac_description()
##
##print Yersinia_pestis.define_genome()[1]
##print Yersinia_pestis.bac_description()
##
##print Pectobacterium_carotovorum.define_genome()[1]
##print Pectobacterium_carotovorum.bac_description()
##
