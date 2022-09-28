from rest_framework.response import Response
from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework import status

import logging

logger = logging.getLogger('django')


def custom_exception_handler(exc, context):
    """
    自定义异常处理
    :param exc: 本次请求发生的异常信息
    :param context: 本次请求发送异常的执行上下文[包括了： 本次请求的对象，异常发送的时间，行号等...]
    :return:
    """
    response = exception_handler(exc, context)
    if response is None:
        view = context['view']
        if isinstance(exc, DatabaseError):
            # 数据库异常(可以查看log的文档关于logging的调用）
            logger.error('[%s] %s' %(view, exc))
            # from rest_framework import status，status文件中包含了状态码的
            response = Response({'message' : '服务器内部错误, 请联系客服工作人员！'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return response