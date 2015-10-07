import pydoop.hdfs as hdfs
import config.hdfs

with hdfs.open(config.hdfs['ur']) as f:
    for line in f:
        print(line)

