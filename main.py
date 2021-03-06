# -*- coding: utf-8 -*-
'''
Created on 2013-1-5

@author: huanghu
'''
import os
from readProperties import saveProperties

class Main():
    
    def init(self):
        self.workflow_path;
        self.target_path;
        self.project_path;
    
    def deploy(self):
        #ebsid
        project_path = "D:\java\program\ErpToOracle\ebsdi";
        
        #maven
        pom_path = project_path + "\pom.xml";
        os.system("mvn package -f " + pom_path);
        
        self.copy();
        
    def copy(self):
        ''''''
        self.getPath();
        self.deleteMkdir();
        self.copyXml();
        self.copyJar();


    def deleteMkdir(self):
        command = "rd " + self.target_path + " /s /q";
        os.system(command);
        
    def copyXml(self):
        command = "xcopy /s " + self.workflow_path + " " + self.target_path;
        print command
        os.system(command);
        
    def copyJar(self):
        appsJar_path = self.project_path + "\\ebsdi-apps\\target\\ebsdi-apps.jar";
        domainJar_path = self.project_path + "\\ebsdi-domain\\target\\ebsdi-domain.jar";
        coreJar_path = self.project_path + "\\ebsdi-core\\target\\ebsdi-core.jar";
        target_lib_path = self.target_path + "lib\\";
        
        command = "xcopy " + appsJar_path + " " + target_lib_path;
        os.system(command);
        
        command = "xcopy " + domainJar_path + " " + target_lib_path;
        os.system(command);
        
        command = "xcopy " + coreJar_path + " " + target_lib_path;
        os.system(command);

    def getPath(self):
        save = saveProperties();
        items = save.read();
        self.workflow_path = self.formatStr(items["workflow_path"]);
        self.target_path = self.formatStr(items["target_path"]);
        self.project_path = self.formatStr(items["project_path"]);
        
    def formatStr(self ,item):
        #item_f = item.decode('unicode_escape').strip();
        item_f = item.decode('utf-8').encode('gbk').strip();
        return item_f;
        
    def test(self):
        command = "xcopy " + self.workflow_path + " " + self.target_path;
        os.system(command);
    
if __name__ == '__main__':
    m = Main();
    m.copy()
