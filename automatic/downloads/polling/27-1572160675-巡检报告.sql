1.数据表巡检项:
1.1 统计数据库存储引擎的数量:
   table_schema:dt_query         engine:InnoDB          engine_counts: 3 
   table_schema:dt_query         engine:MyISAM          engine_counts: 8 
   table_schema:repl_monitor     engine:InnoDB          engine_counts: 2 
   table_schema:sbtest           engine:InnoDB          engine_counts:10 
   table_schema:terrace_db       engine:InnoDB          engine_counts:23 
   table_schema:zst              engine:InnoDB          engine_counts: 9 
1.2 超过多少G的大表:
   table_schema:dt_query         table_name:tamzsaleranks                            size:788.64M
   table_schema:zst              table_name:t1_1yi                                   size:2218.00M
   table_schema:zst              table_name:t1_10yi                                  size:1309.00M
   table_schema:dt_query         table_name:tamz_sale_ranks                          size:1062.55M
1.3 数据量排名前靠前的大表:
   table_schema:zst              table_name:t1_1yi                                   all_size:2218.00M        data_size:2218.00M        index_size:0.00M           table_rows:95674500
   table_schema:zst              table_name:t1_10yi                                  all_size:1309.00M        data_size:1309.00M        index_size:0.00M           table_rows:56484099
   table_schema:dt_query         table_name:tamz_sale_ranks                          all_size:1062.55M        data_size:811.00M         index_size:251.55M         table_rows:4014141
1.4 单表超过行数 100000 表:
   table_schema:zst             table_name:t1_1yi                                   table_rows:95674500 
   table_schema:zst             table_name:t1_10yi                                  table_rows:56484099 
   table_schema:dt_query        table_name:tamzsaleranks                            table_rows:4095592 
   table_schema:dt_query        table_name:tamz_sale_ranks                          table_rows:4014141 
   table_schema:dt_query        table_name:cron_origin                              table_rows:975246 
   table_schema:dt_query        table_name:cron_result                              table_rows:288792 
   table_schema:sbtest          table_name:sbtest8                                  table_rows:196982 
   table_schema:sbtest          table_name:sbtest4                                  table_rows:189339 
   table_schema:sbtest          table_name:sbtest6                                  table_rows:184937 
   table_schema:sbtest          table_name:sbtest5                                  table_rows:183016 
   table_schema:sbtest          table_name:sbtest3                                  table_rows:179437 
   table_schema:sbtest          table_name:sbtest9                                  table_rows:178798 
   table_schema:sbtest          table_name:sbtest1                                  table_rows:177128 
   table_schema:sbtest          table_name:sbtest10                                 table_rows:176353 
   table_schema:sbtest          table_name:sbtest2                                  table_rows:172682 
   table_schema:sbtest          table_name:sbtest7                                  table_rows:169987 
1.5 自增ID占比大于 5.0% 的表 :
   ###没有自增ID占比大于 5.0% 的表###
1.6 碎片大于多少 0.5G 的表 :
   ###没有碎片大于多少 0.5G 的表###
1.7 统计大字段表:
    table_schema:repl_monitor     engine:slave_statment                 engine_counts:last_sql_error  
    table_schema:repl_monitor     engine:slave_statment                 engine_counts:slave_sql_running_state 
1.8 统计字段类型varchar长度大于 50 的表:
    table_schema:dt_query        table_name:ag_zhenren_zz                            column_name:result               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:dt_query        table_name:agbetdetail                              column_name:stringex             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:dt_query        table_name:agbetdetail                              column_name:remark               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:dt_query        table_name:agxmlconfig                              column_name:fileName             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:dt_query        table_name:ban_ip                                   column_name:why                  data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:dt_query        table_name:tamz_sale_ranks                          column_name:FGroupName           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:dt_query        table_name:tamz_sale_ranks                          column_name:FItemName            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:2048
    table_schema:dt_query        table_name:tamzsaleranks                            column_name:FGroupName           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:dt_query        table_name:tamzsaleranks                            column_name:FItemName            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:2048
    table_schema:repl_monitor    table_name:master_statment                          column_name:executed_gtid_set    data_type:varchar              CHARACTER_MAXIMUM_LENGTH:60
    table_schema:repl_monitor    table_name:slave_statment                           column_name:executed_gtid_set    data_type:varchar              CHARACTER_MAXIMUM_LENGTH:60
    table_schema:terrace_db      table_name:auth_group                               column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:80
    table_schema:terrace_db      table_name:auth_permission                          column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:terrace_db      table_name:auth_permission                          column_name:codename             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:auth_user                                column_name:password             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:128
    table_schema:terrace_db      table_name:auth_user                                column_name:username             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:150
    table_schema:terrace_db      table_name:auth_user                                column_name:last_name            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:150
    table_schema:terrace_db      table_name:auth_user                                column_name:email                data_type:varchar              CHARACTER_MAXIMUM_LENGTH:254
    table_schema:terrace_db      table_name:django_admin_log                         column_name:object_repr          data_type:varchar              CHARACTER_MAXIMUM_LENGTH:200
    table_schema:terrace_db      table_name:django_celery_results_taskresult         column_name:task_id              data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:terrace_db      table_name:django_celery_results_taskresult         column_name:content_type         data_type:varchar              CHARACTER_MAXIMUM_LENGTH:128
    table_schema:terrace_db      table_name:django_celery_results_taskresult         column_name:content_encoding     data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:terrace_db      table_name:django_celery_results_taskresult         column_name:task_name            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:terrace_db      table_name:django_content_type                      column_name:app_label            data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:django_content_type                      column_name:model                data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:django_migrations                        column_name:app                  data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:terrace_db      table_name:django_migrations                        column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:terrace_db      table_name:django_q_ormq                            column_name:key                  data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:django_q_schedule                        column_name:func                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:terrace_db      table_name:django_q_schedule                        column_name:hook                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:terrace_db      table_name:django_q_schedule                        column_name:task                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:django_q_schedule                        column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:django_q_task                            column_name:name                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:django_q_task                            column_name:func                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:terrace_db      table_name:django_q_task                            column_name:hook                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:256
    table_schema:terrace_db      table_name:django_q_task                            column_name:group                data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:myapp_db_instance                        column_name:password             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:300
    table_schema:terrace_db      table_name:myapp_db_instance                        column_name:user                 data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:mysql_slow_query_review_history          column_name:hostname_max         data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:terrace_db      table_name:mysql_slow_query_review_history          column_name:client_max           data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:terrace_db      table_name:mysql_slow_query_review_history          column_name:user_max             data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:terrace_db      table_name:mysql_slow_query_review_history          column_name:db_max               data_type:varchar              CHARACTER_MAXIMUM_LENGTH:64
    table_schema:terrace_db      table_name:salt_record                              column_name:jid                  data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
    table_schema:terrace_db      table_name:salt_record                              column_name:tgt                  data_type:varchar              CHARACTER_MAXIMUM_LENGTH:100
    table_schema:terrace_db      table_name:tb_blacklist                             column_name:dbtag                data_type:varchar              CHARACTER_MAXIMUM_LENGTH:255
2.索引巡检项:
2.1 获取索引数目大于 3 个的表:
   ###没有索引数目大于3个的表###
2.2 获取没有主键索引的表:
   ###没有主键索引的表###
3.参数巡检项:
3.1 InnoDB层参数:
3.1.1 InnoDB层缓冲池参数:
    innodb_buffer_pool_dump_at_shutdown : ON
    innodb_buffer_pool_instances : 1
    innodb_buffer_pool_load_at_startup : ON
    innodb_buffer_pool_size : 104857600
    innodb_flush_neighbors : 1
    innodb_lru_scan_depth : 1024
    innodb_max_dirty_pages_pct : 50.000000
    innodb_old_blocks_pct : 37
    innodb_old_blocks_time : 1000
    innodb_random_read_ahead : OFF
    innodb_read_ahead_threshold : 56
3.1.2 InnoDB层redo参数:
    innodb_flush_log_at_trx_commit : 2
    innodb_log_buffer_size : 8388608
    innodb_log_file_size : 104857600
    innodb_log_files_in_group : 3
3.1.3 InnoDB层持久化统计信息参数:
    innodb_stats_auto_recalc : ON
    innodb_stats_persistent : ON
    innodb_stats_persistent_sample_pages : 20
3.1.4 InnoDB层其它参数:
    innodb_adaptive_hash_index : ON
    innodb_autoinc_lock_mode : 1
    innodb_change_buffer_max_size : 25
    innodb_change_buffering : all
    innodb_data_file_path : ibdata1:100M:autoextend
    innodb_data_home_dir : 
    innodb_doublewrite : ON
    innodb_fast_shutdown : 1
    innodb_file_per_table : ON
    innodb_flush_method : O_DIRECT
    innodb_force_recovery : 0
    innodb_io_capacity : 2000
    innodb_io_capacity_max : 4000
    innodb_lock_wait_timeout : 50
    innodb_open_files : 2048
    innodb_page_cleaners : 1
    innodb_purge_threads : 4
    innodb_read_io_threads : 4
    innodb_rollback_on_timeout : ON
    innodb_thread_concurrency : 0
    innodb_write_io_threads : 4
3.2 Server层参数:
3.2.1 Server层binlog参数:
    binlog_cache_size : 32768
    binlog_format : ROW
    binlog_group_commit_sync_delay : 0
    binlog_group_commit_sync_no_delay_count : 0
    binlog_row_image : FULL
    expire_logs_days : 10
    max_binlog_cache_size : 18446744073709547520
    max_binlog_size : 268435456
    sync_binlog : 0
3.2.2 Server层线程/会话相关的内存参数:
    join_buffer_size : 131072
    key_buffer_size : 8388608
    query_cache_size : 0
    read_buffer_size : 2097152
    read_rnd_buffer_size : 16777216
    sort_buffer_size : 131072
    tmp_table_size : 100663296
3.2.3 Server层其它参数:
    interactive_timeout : 300
    log_queries_not_using_indexes : OFF
    log_timestamps : UTC
    long_query_time : 1.000000
    lower_case_table_names : 1
    max_allowed_packet : 4194304
    max_connect_errors : 100000
    max_connections : 100
    max_execution_time : 0
    max_user_connections : 0
    net_buffer_length : 16384
    open_files_limit : 65535
    slow_query_log : ON
    sql_mode : ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
    system_time_zone : CST
    table_open_cache : 2048
    time_zone : SYSTEM
    wait_timeout : 300
4 状态巡检项:
4.1 InnoDB层缓冲池状态:
   Innodb_buffer_pool_pages_data : 3812
   Innodb_buffer_pool_pages_dirty : 12
   Innodb_buffer_pool_pages_flushed : 2902
   Innodb_buffer_pool_pages_free : 2585
   Innodb_buffer_pool_pages_total : 6400
   Innodb_buffer_pool_read_ahead : 1280
   Innodb_buffer_pool_read_ahead_evicted : 0
   Innodb_buffer_pool_read_requests : 891495
   Innodb_buffer_pool_reads : 2375
   Innodb_buffer_pool_wait_free : 0
   脏页在缓冲池数据页中的占比为: 0.19%
   InnoDB buffer pool 缓冲池命中率: 99.59%
4.2 并发线程连接数:
   Threads_connected : 5
   Threads_created : 14
   Threads_running : 1
4.3 InnoDB行锁等待:
   Innodb_row_lock_current_waits : 0
   Innodb_row_lock_time : 0
   Innodb_row_lock_time_avg : 0
   Innodb_row_lock_time_max : 0
   Innodb_row_lock_waits : 0
4.4 打开表的次数:
   Open_files : 101
   Open_tables : 1980
   Opened_tables : 8556
4.5 创建内存临时表和磁盘临时表的次数:
   Created_tmp_disk_tables : 1026
   Created_tmp_tables : 9061
4.6 InnoDB关键特性double write的使用情况:
   Innodb_dblwr_pages_written : 2346
   Innodb_dblwr_writes : 149
   每次写操作合并page的个数: 16.0
