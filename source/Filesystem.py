import os
import shutil
from random import randint
from Util import *
from Process import *

class Filesystem:
    @staticmethod
    def fileExists(filename):
        return os.path.isfile(filename)



    @staticmethod
    def readFile(filename):
        try:
            f = open(filename,"r")
            fileContent = f.read()
            f.close()
        except Exception:
            return ""

        return fileContent



    @staticmethod
    def writeFile(filename,content):
        try:
            f = open(filename,"w")
            f.write(content+"\n")
            f.close()

            os.chmod(filename,0700)
        except Exception:
            return False

        return True



    @staticmethod
    def moveAs(fromFile,toFile):
        try:
            shutil.move(fromFile,toFile)
        except Exception:
            return False

        return True



    @staticmethod
    def fileSize(filename):
        try:
            fSize = os.path.getsize(filename)
        except Exception:
            return 0

        return fSize



    @staticmethod
    def dirSize(folder):
        dSize = 0

        try:
            for dirpath, dirnames, filenames in os.walk(folder):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    if not os.path.islink(fp): # skip if it is symbolic link.
                        dSize += os.path.getsize(fp)
        except Exception:
            return 0

        return dSize



    @staticmethod
    def tmpMount(devicePartition):
        r = str(randint(1,9999))
        tempFolder = "/tmp/mnt__"+r

        if Process.execute("mkdir "+tempFolder+" && mount "+devicePartition+" "+tempFolder+"; sleep 2")["success"]:
            return tempFolder

        return ""



    @staticmethod
    def tmpUmount(mountpoint):
        if not Process.execute("sync; umount "+mountpoint+" && rm -fR "+mountpoint+"; sleep 2")["success"]:
            return False

        return True



    @staticmethod
    def getSystemPartitionMountpoint():
        getSystemPartitionMountpoint = ""

        getSystemPartitionMountpointCmdln = "mount | grep iso9660 | grep live | awk '{print $3}'"
        getSystemPartitionMountpointRun = Process.execute(getSystemPartitionMountpointCmdln)

        if getSystemPartitionMountpointRun["success"]:
            getSystemPartitionMountpoint = getSystemPartitionMountpointRun["output"]

        return getSystemPartitionMountpoint



    @staticmethod
    def createIsoFile(sourceFolder):
        isoFilename = ""

        if Filesystem.fileExists("/resilientlinux.iso"):
            isoFilename = "/resilientlinux.iso"
        else:
            createIsoFileCmdln = "xorrisofs -v -J -r -V RESILIENT_LINUX -o /resilientlinux.iso "+sourceFolder
            if Process.execute(createIsoFileCmdln)["success"]:
                isoFilename = "/resilientlinux.iso"

        return isoFilename

