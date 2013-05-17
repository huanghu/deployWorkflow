主要实现的功能是将mvn编译后的文件（jar）和oozie的配置文件拷贝入一个指定的目录，
这个目录就是提交到jira的测试版本（工具只实现复制到指定目录功能，并未把目录打为zip包）。

注意：
1.打包之前会把目标目录删掉，所以建议release.txt放到ebsdi-apps/resource/的相关目录里。
2.在path_properties里设置相关路径。
3.以后看能不能打成一个exe包。

执行方式：
cmd-->python main.py
