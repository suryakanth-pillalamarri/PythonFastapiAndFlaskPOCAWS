
# import string
import os
import time

#create a python file that should be able to create 100 random text files rename and delete all the files.
class FileOperations:

    def __init__(self,folder_path):
        self.folder_path=folder_path

    # def give_file_name(self,length):

    #     #including letters and digits
    #     # if digita are needed i can add string.digits
    #     chars=string.ascii_letters
    #     #print(random.choices(chars,k=length))
    #     filename=''.join(random.choices(chars,k=length))
    #     return filename

    def create_file(self,filename):
        try:
            #filename=self.give_file_name(8)
            filepath=os.path.join(self.folder_path,filename)
            filepath=filepath+".txt"
            print(filepath)
            #print("rama")
            if not os.path.exists(filepath):

                data="this is randome file with file name"+" "+filename
                with open(filepath,'w') as file:
                    file.write(data)
            
                return f"file created at path {filepath}"
            else:
                return "file already exists"

        
        except Exception as e:
            return ("Error in creating file")
        

    def rename_file(self,old_name,new_name):
        print("Sri rama")
        try:
            print(old_name)
            print(new_name)
            filepath=os.path.join(self.folder_path,old_name)
            
            print(filepath)

            if os.path.exists(filepath):
                print('vasudeva')
                os.rename(filepath, os.path.join(self.folder_path, new_name))
                return f"file renamed from {old_name} to {new_name} successfully :()"
            else:
                return f"{old_name} does not exists"
        except Exception as e:
            return "Some error occurred"
        

    def rename_all_the_files(self,new_prefix):
        try:
            files=os.listdir(self.folder_path)
            for file_name in files:
                old_file_path=os.path.join(self.folder_path,file_name)
                # print("old_file_path",old_file_path)
                new_file_name=new_prefix+"_"+file_name
                # print("new_file_name",new_file_name)
                # print(new_file_name)
                os.rename(old_file_path,os.path.join(self.folder_path,new_file_name))
            return "All files renamed successfully."
        except Exception as e:
            return f"Error while renaming the files{e}"
    def delete_files(self):
        try:
            files=os.listdir(self.folder_path)
            for file_name in files:
                filepath=os.path.join(self.folder_path,file_name)
                #checking if file exists and it is rgular file
                if os.path.exists(filepath) and os.path.isfile(filepath):
                    os.remove(filepath)
            return "All files removed successfully"
        except Exception as e:
            return  "Error occured while deleting files"
    



input_path=r"D:\Surya files\pythonaws_poc_2024\second_problem\test_folder"
try:
    if  not os.path.exists(input_path):
        raise FileNotFoundError
    fo=FileOperations(input_path)
    for i in range(1,101):
        print(fo.create_file(str(i)))

    time.sleep(5)

    print(fo.rename_all_the_files("new"))

    time.sleep(5)

    print(fo.delete_files())
    
except FileNotFoundError as f:
    print("Folder does not exists")

#print(fo.rename_file("100.txt","100(1).txt"))

# f1=FileOperations(input_path)
# print(f1.rename_file("abc.txt","1(1).txt"))