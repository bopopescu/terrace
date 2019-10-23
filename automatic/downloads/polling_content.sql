

1. 数据表巡检项:
    1.1 统计数据库实例存储引擎的类型的数量
    1.2 超过 多少 G 的大表
    1.3 数据量排名前 多少 的表
    1.4 单表超过行数 多少 的表:
    1.5 自增ID占比大于 多少 的表
    1.6 碎片大于多少 G 的表
    1.7 统计大字段表
    1.8 统计字段类型varchar长度大于 多少 的表


2. 索引巡检项
    2.1 获取索引数目大于 多少 个的表
    2.2 获取没有主键索引的表

3. 参数巡检项:
	3.1 InnoDB层参数
        3.1.1 InnoDB层缓冲池参数
        3.1.2 InnoDB层redo参数
        3.1.3 InnoDB层持久化统计信息参数
        3.1.4 InnoDB层其它参数

        3.2 Server层参数
        3.2.1 Server层binlog参数
        3.2.2 Server层线程/会话相关的内存参数
        3.2.3 Server层其它参数
	
4. 状态巡检项
	4.1 InnoDB层缓冲池状态值
	4.2 并发线程连接数
	4.3 InnoDB行锁等待
	4.4 打开表的次数
	4.5 创建内存临时表和磁盘临时表的次数
	4.6 InnoDB关键特性double write的使用情况
	4.7 因log buffer不足导致等待的次数
	
		
5. 其它巡检项
	5.1 使用到内存临时表或者磁盘临时表的前多少个SQL
	5.2 获取执行时间大于多少秒的长事务
	5.3 行锁等待列表