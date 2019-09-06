from django.shortcuts import render

# Create your views here.
def mgmt_files(request): #列出树形目录，上传文件页面
    if request.method == 'POST':
        path_root = "D:\\py\\ITFiles" #上传文件的主目录
        myFile =request.FILES.get("file", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not myFile:  
            dstatus = "请选择需要上传的文件!"
        else:
            path_ostype = os.path.join(path_root,request.POST.get("ostype"))
            path_dst_file = os.path.join(path_ostype,myFile.name)
            # print path_dst_file
            if os.path.isfile(path_dst_file):
                dstatus = "%s 已存在!"%(myFile.name)
            else:
                destination = open(path_dst_file,'wb+')    # 打开特定的文件进行二进制的写操作  
                for chunk in myFile.chunks():      # 分块写入文件  
                    destination.write(chunk)  
                destination.close()  
                dstatus = "%s 上传成功!"%(myFile.name)
        return HttpResponse(str(dstatus))

    return render(request,'sinfors/mgmt_files.html')

def mgmt_file_download(request,*args,**kwargs): #提供文件下载页面
    #定义文件分块下载函数 
    def file_iterator(file_name, chunk_size=512):
        with open(file_name,'rb') as f: #如果不加‘rb’以二进制方式打开，文件流中遇到特殊字符会终止下载，下载下来的文件不完整
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    path_root = "D:\\py\\ITFiles"
    if kwargs['fpath'] is not None and kwargs['fname'] is not None:
        file_fpath = os.path.join(path_root,kwargs['fpath']) #kwargs['fapth']是文件的上一级目录名称
        file_dstpath = os.path.join(file_fpath,kwargs['fname']) #kwargs['fname']是文件名称

        response = StreamingHttpResponse(file_iterator(file_dstpath))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(kwargs['fname']) #此处kwargs['fname']是要下载的文件的文件名称
        return response