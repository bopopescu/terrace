# -*- coding: UTF-8 -*-
import logging
import os
import time
import traceback
import json

from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from myapp.common.utils.rewrite_json_encoder import RewriteJsonEncoder
from myapp.models import Db_instance

from myapp.engines import get_engine
from myapp.include.polling_settings import innodb_buffer_pool_param,innodb_redo_log_param,innodb_persistent_param,innodb_other_param
from myapp.include.polling_settings import server_binlog_param,server_thread_session_param,server_other_param
from myapp.include.polling_settings import innodb_buffer_pool_status_list,innodb_threads_connection_status_list,\
    innodb_row_lock_status_list,innodb_open_status_list,innodb_create_tmp_table_status_list,innodb_double_write_status_list


from myapp.include.polling_sql import get_table_schema_engine, get_table_size, get_top_big_tables, get_table_rows, get_auto_increment_ratio,\
    get_big_fragment_tables, get_table_big_column, get_table_long_varchar_column, get_too_much_columns_indexs, get_not_primary_index


logger = logging.getLogger('default')

def download_polling_report(request):

    instance_id = request.POST.get("instance_id")
    try:
        instance = Db_instance.objects.get(id=int(instance_id))
    except Db_instance.DoesNotExist:
        res = {'status': 0, 'msg': '实例不存在'}
        return HttpResponse(json.dumps(res))
    instance_name = instance.instance_name
    query_engine = get_engine(instance=instance)

    timestamp = int(time.time())
    path = os.path.join(settings.BASE_DIR, 'downloads/polling/')
    filename = os.path.join(path, f"{instance_name}的巡检报告{timestamp}.sql")
    res = {'status': 0, 'msg': '数据库巡检报告已经下载到项目的downloads文件夹下'}

    get_table_size_custom = 0.0000001
    top_big_tables_custom = 20
    table_row_custom = 20000000
    auto_increment_ratio_custom = 0.1001
    fragment_size_custom = 0.000001
    character_maximum_length_custom = 500
    index_counts_custom = 3
    try:
        buffer_pool_value            = query_engine.get_variables(innodb_buffer_pool_param).rows
        redo_log_value               = query_engine.get_variables(innodb_redo_log_param).rows
        persistent_value             = query_engine.get_variables(innodb_persistent_param).rows
        innodb_other_value           = query_engine.get_variables(innodb_other_param).rows
        server_binlog_value          = query_engine.get_variables(server_binlog_param).rows
        server_thread_session_value  = query_engine.get_variables(server_thread_session_param).rows
        server_other_value           = query_engine.get_variables(server_other_param).rows

        get_table_schema_engine_data = query_engine.query_set(sql=get_table_schema_engine()).rows
        get_table_size_data          = query_engine.query_set(sql=get_table_size(get_table_size_custom)).rows
        get_top_big_tables_data      = query_engine.query_set(sql=get_top_big_tables(top_big_tables_custom)).rows
        get_table_rows_data          = query_engine.query_set(sql=get_table_rows(table_row_custom))
        get_auto_increment_ratio_data = query_engine.query_set(sql=get_auto_increment_ratio(auto_increment_ratio_custom))
        get_big_fragment_tables_data = query_engine.query_set(sql=get_big_fragment_tables(fragment_size_custom))
        get_table_big_column_data    = query_engine.query_set(sql=get_table_big_column())

        get_long_varchar_column_data = query_engine.query_set(sql=get_table_long_varchar_column(character_maximum_length_custom))
        get_too_much_columns_indexs_data  = query_engine.query_set(sql=get_too_much_columns_indexs(index_counts_custom))
        get_not_primary_index_data   = query_engine.query_set(sql=get_not_primary_index())

        innodb_buffer_pool_status    = query_engine.get_status(innodb_buffer_pool_status_list).rows
        innodb_threads_connection_status = query_engine.get_status(innodb_threads_connection_status_list).rows
        innodb_row_lock_status       = query_engine.get_status(innodb_row_lock_status_list).rows
        innodb_open_status           = query_engine.get_status(innodb_open_status_list).rows
        innodb_create_tmp_table_status = query_engine.get_status(innodb_create_tmp_table_status_list).rows
        innodb_double_write_status   = query_engine.get_status(innodb_double_write_status_list).rows

        with open(filename, 'a+') as f:
            f.write('4. 状态巡检项:' + '\n')
            f.write('4.1 InnoDB层缓冲池状态:' + '\n')

            for v in innodb_buffer_pool_status:

                f.write('   {} : {}'.format(v[0], v[1]) + '\n')

                if v[0] == 'Innodb_buffer_pool_pages_dirty':
                    innodb_buffer_pool_pages_dirty = v[1]
                else:
                    innodb_buffer_pool_pages_dirty = None

                if v[0] == 'Innodb_buffer_pool_pages_total':
                    innodb_buffer_pool_pages_total = v[1]
                else:
                    innodb_buffer_pool_pages_total = None

                if innodb_buffer_pool_pages_dirty is not None and innodb_buffer_pool_pages_total is not None:
                    dirty_page = round(int(innodb_buffer_pool_pages_dirty) / int(innodb_buffer_pool_pages_total), 4)
                    f.write('   脏页在缓冲池数据页中的占比为: {}%'.format(dirty_page * 100) + '\n')

                if v[0] == 'Innodb_buffer_pool_read_requests':
                    innodb_buffer_pool_read_requests = v[1]
                else:
                    innodb_buffer_pool_read_requests = None

                if v[0] == 'Innodb_buffer_pool_read_ahead':
                    innodb_buffer_pool_read_ahead = v[1]
                else:
                    innodb_buffer_pool_read_ahead = None

                if v[0] == 'innodb_buffer_pool_reads':
                    innodb_buffer_pool_reads = v[1]
                else:
                    innodb_buffer_pool_reads = None

                if innodb_buffer_pool_read_requests is not None and innodb_buffer_pool_read_ahead is not None and innodb_buffer_pool_reads is not None:
                    ibp_hit = round(int(innodb_buffer_pool_read_requests) / (int(innodb_buffer_pool_read_requests) + int(innodb_buffer_pool_read_ahead) + int(innodb_buffer_pool_reads)),4)
                    f.write('InnoDB buffer pool 命中率: {}%'.format(ibp_hit * 100) + '\n')


            """
            ibp_pages_dirty = get_status_value(insname, 'innodb_buffer_pool_pages_dirty', 0)
            ibp_pages_total = get_status_value(insname, 'innodb_buffer_pool_pages_total', 0)
            dirty_page = round(int(ibp_pages_dirty) / int(ibp_pages_total), 4)
            f.write('脏页在缓冲池数据页中的占比为: {}%'.format(dirty_page * 100) + '\n')

            ibp_read_requests = get_status_value(insname, 'innodb_buffer_pool_read_requests', 0)
            ibp_read_ahead = get_status_value(insname, 'innodb_buffer_pool_read_ahead', 0)
            ibp_read_reads = get_status_value(insname, 'innodb_buffer_pool_reads', 0)
           

            ibp_wait_free = get_status_value(insname, 'Innodb_buffer_pool_wait_free', 0)
            if int(ibp_wait_free) > 0:
                f.write('注意：InnoDB Buffer Pool可能不够用了，需要详细检查并处理，目前等待申请空闲列表的次数为: {} 次'.format(ibp_wait_free) + '\n')
            """


            f.write('4.2 并发线程连接数:' + '\n')
            for v in innodb_threads_connection_status:
                f.write('   {} : {}'.format(v[0], v[1]) + '\n')

            f.write('4.3 InnoDB行锁等待:' + '\n')
            for v in innodb_row_lock_status:
                f.write('   {} : {}'.format(v[0], v[1]) + '\n')

            f.write('4.4 打开表的次数:' + '\n')
            for v in innodb_open_status:
                f.write('   {} : {}'.format(v[0], v[1]) + '\n')

            f.write('4.5 创建内存临时表和磁盘临时表的次数:' + '\n')
            for v in innodb_create_tmp_table_status:
                f.write('   {} : {}'.format(v[0], v[1]) + '\n')

            f.write('4.6 InnoDB关键特性double write的使用情况:' + '\n')
            for v in innodb_double_write_status:
                f.write('   {} : {}'.format(v[0], v[1]) + '\n')

            f.write('1.数据表巡检项:' + '\n')
            f.write('1.1 统计数据库存储引擎的数量:' + '\n')
            for val in get_table_schema_engine_data:
                row = '   table_schema:{:15s}  engine:{:15s} engine_counts:{:2} '.format(val[0], val[1], val[2])
                f.write(row + '\n')

            f.write('1.2 超过多少G的大表:' + '\n')
            for val in get_table_size_data:
                row = '   table_schema:{:15s}  table_name:{:40s} size:{:2s}'.format(val[0], val[1], val[2])
                f.write(row + '\n')

            f.write('1.3 数据量排名前靠前的大表:' + '\n')
            for val in get_top_big_tables_data:
                  row = '   table_schema:{:15s}  table_name:{:40s} all_size:{:15s} data_size:{:15s} index_size:{:15s} table_rows:{:5}'.format(
                      val[0], val[1], val[2], val[3], val[4], val[5])
                  f.write(row + '\n')


            f.write('1.4 单表超过行数 {} 表:'.format(table_row_custom) + '\n')
            if get_table_rows_data.effect_row > 0:
                for val in get_table_rows_data.rows:
                    row = '   table_schema:{:15s} table_name:{:40s} table_rows:{} '.format(val[0], val[1], val[2])
                    f.write(row + '\n')
            else:
                f.write('   ###没有单表超过行数 {} 表###'.format(table_row_custom) + '\n')


            auto_increment_format = '{}{}'.format(auto_increment_ratio_custom * 100, '%')
            f.write('1.5 自增ID占比大于 {} 的表 :'.format(auto_increment_format) + '\n')
            if get_auto_increment_ratio_data.effect_row > 0:
                for val in get_auto_increment_ratio_data.rows:
                    row = '   table_schema:{:15s} table_name:{:40s} auto_increment_ratio:{} max_value:{} auto_increment:{}'.format(val[0], val[1], val[2], val[3], val[4])
                    f.write(row + '\n')
            else:
                f.write('   ###没有自增ID占比大于 {} 的表###'.format(auto_increment_format) + '\n')


            f.write('1.6 碎片大于多少 {}G 的表 :'.format(fragment_size_custom) + '\n')
            if get_big_fragment_tables_data.effect_row > 0:
                for val in get_big_fragment_tables_data.rows:
                    row = '{} table_schema:{:15s}  table_name:{:40s} fragment:{:10s}'. format('    ', val[0], val[1], val[2])
                    f.write(row + '\n')
            else:
                f.write('{} ###没有碎片大于多少 {}G 的表###'.format('   ', fragment_size_custom) + '\n')

            f.write('1.7 统计大字段表:' + '\n')
            if get_table_big_column_data.effect_row > 0:
                for val in get_table_big_column_data.rows:
                    row = '{} table_schema:{:15s}  engine:{:30s} engine_counts:{:15} '.format('   ', val[0], val[1], val[2])
                    f.write(row + '\n')
            else:
                f.write('    ###没有大字段表###' + '\n')

            f.write('1.8 统计字段类型varchar长度大于 {} 的表:'.format(character_maximum_length_custom) + '\n')
            if get_long_varchar_column_data.effect_row > 0:
                for val in get_long_varchar_column_data.rows:
                    row = '    table_schema:{:15} table_name:{:40s} column_name:{:20s} data_type:{:20s} CHARACTER_MAXIMUM_LENGTH:{:2}'.format(val[0], val[1], val[2], val[3], val[4])
                    f.write(row + '\n')
            else:
                f.write('  ###没有字段类型varchar长度大于 {} 的表###'.format(character_maximum_length_custom) + '\n')

            f.write('2.索引巡检项:' + '\n')


            f.write('2.1 获取索引数目大于 {} 个的表:' .format(index_counts_custom) + '\n')
            if get_too_much_columns_indexs_data.effect_row > 0:
                for val in get_too_much_columns_indexs_data.rows:
                    row = '   table_schema: {:15s}  table_name: {:40s} ecolumn_name: {:20s} index_nam: {:2s} '.format(val[0], val[1], val[2], val[3])
                    f.write(row + '\n')
            else:
                f.write('   ###没有索引数目大于5的表###' .format(index_counts_custom) + '\n')

            f.write('2.2 获取没有主键索引的表:' + '\n')
            if get_not_primary_index_data.effect_row > 0:
                for val in get_not_primary_index_data.rows:
                    row =    'table_schema:{:15s}  table_name:{:40s} '.format(val[0], val[1])
                    f.write(row + '\n')
            else:
                f.write('   ###没有主键索引的表###' + '\n')


            f.write('3.参数巡检项:' + '\n')
            f.write('3.1 InnoDB层参数:' + '\n')

            f.write('3.1.1 InnoDB层缓冲池参数:' + '\n')
            for v in buffer_pool_value:
                f.write('{} {} : {}'.format('   ', v[0], v[1]) + '\n')

            f.write('3.1.2 InnoDB层redo参数:' + '\n')
            for v in redo_log_value:
                f.write('{} {} : {}'.format('   ', v[0], v[1]) + '\n')

            f.write('3.1.3 InnoDB层持久化统计信息参数:' + '\n')
            for v in persistent_value:
                f.write('{} {} : {}'.format('   ', v[0], v[1]) + '\n')

            f.write('3.1.4 InnoDB层其它参数:' + '\n')
            for v in innodb_other_value:
                f.write('{} {} : {}'.format('   ', v[0], v[1]) + '\n')

            f.write('3.2 Server层参数:' + '\n')

            f.write('3.2.1 Server层binlog参数:' + '\n')
            for v in server_binlog_value:
                f.write('{} {} : {}'.format('   ', v[0], v[1]) + '\n')

            f.write('3.2.2 Server层线程/会话相关的内存参数:' + '\n')
            for v in server_thread_session_value:
                f.write('{} {} : {}'.format('   ', v[0], v[1]) + '\n')

            f.write('3.2.3 Server层其它参数:' + '\n')
            for v in server_other_value:
                f.write('{} {} : {}'.format('   ', v[0], v[1]) + '\n')

            f.write('4 状态巡检项:' + '\n')
            f.write('4.1 InnoDB层缓冲池状态值:' + '\n')



    except Exception as err:
        logger.error(f'错误信息：{traceback.format_exc()}')
        res['status'] = 1
        res['msg'] = str(err)

    return HttpResponse(json.dumps(res), content_type='application/json')


def polling_list(request):

    instance_name = request.POST.get('instance_name')
    type = request.POST.get('type',)
    db_type = request.POST.get('db_type')
    limit = int(request.POST.get('limit'))
    offset = int(request.POST.get('offset'))

    instance_obj = Db_instance.objects.all()

    if instance_name != '':
        instance_obj = instance_obj.filter(instance_name__icontains=instance_name)
    if type != '':
        instance_obj = instance_obj.filter(type=type)
    if db_type != '':
        instance_obj = instance_obj.filter(db_type=db_type)

    count = instance_obj.count()
    instance_res = instance_obj[offset:limit].values('id', 'instance_name', 'type', 'db_type', 'host', 'port', )

    # QuerySet 序列化
    rows = [row for row in instance_res]
    result = {"total": count, "rows": rows}

    return HttpResponse(json.dumps(result), content_type='application/json')

