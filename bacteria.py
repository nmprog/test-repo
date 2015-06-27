import webbrowser
from Tkinter import *

import urllib

class Bacteria():
    def __init__(self, bacteria_name, bacteria_description, bacteria_photo,
                 bacteria_chromosome, bacteria_plasmid):
        self.title = bacteria_name
        self.description = bacteria_description
        self.photo_image_url = bacteria_photo
        self.genome_main = bacteria_chromosome
        self.genome_plasmid = bacteria_plasmid
	
    def get_photo(self):
        from PIL import Image
        image = urllib.URLopener()
        output_Filename = self.title + '.jpg'
        image.retrieve(self.photo_image_url,
                       output_Filename)
        print output_Filename
        image1 = Image.open(output_Filename, 'r')
        image2 = image1.save(self.title + ".gif", format = "GIF")
        master = Tk()
##        new_image1 = PhotoImage(file = self.title + ".gif")
##        
##        head = Label(master, text = "Bacterial DNA Analysis")
##        head.pack(side = TOP)
##        Button(master, image = new_image1).grid(row = 3, column = 1)
##        master.mainloop()

        
    def define_genome(self):
        if not(self.genome_main) == None:
            gen_file = self.genome_main
            genome = open(gen_file, 'r')
            gen_str = genome.readline()
            length = len(gen_str)
            genome.close()
        else:
            gen_file = self.genome_plasmid
            genome = open(gen_file, 'r')
            gen_str = genome.readline()
            length = len(gen_str)
            genome.close()
        return genome, length

##    def genome_length(self):
##        return len(genome)

    def bac_description(self):
        bac_description = self.description
        return bac_description

    

	
