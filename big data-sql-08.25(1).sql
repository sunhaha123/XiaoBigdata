目录结构

一级目录
   （1）基本信息
        二级目录：运动员信息、教练员信息、击球动作、人体主要关节点
   （2）训练管理
	二级目录：训练计划、训练强度、生理生化指标、比赛成绩
   （3）动作捕捉
	二级目录：动作捕捉原始数据、关节点发力顺序、动作曲线模型
   （4）击球力量
	二级目录：击球力量原始数据
   （5）击球质量
	二级目录：击球质量数据
   （6）大数据分析及可视化
	动作曲线相似度分析、击球力量数据分析、击球力量差异性分析、击球效果差异性分析、击球力量与击球效果的相关性分析
   （7）系统管理


一、击球力量数据

/*击球动作*/
drop table action;

CREATE TABLE action (
  actionid int(6) NOT NULL,
  name    varchar(20) NOT NULL,
  memo    varchar(20) NOT NULL,
  PRIMARY KEY (actionid)
); 

/*运动员基本信息表*/
drop table athlete;

CREATE TABLE athlete (
  athleteid varchar(10) not NULL,
  name varchar(20) NOT NULL,
  sfzh varchar(20) NOT NULL,
  csrq datetime  DEFAULT NULL,
  gender varchar(2) DEFAULT NULL,
  height decimal(8,2),
  weight decimal(8,2),
  birthplace varchar(200) DEFAULT NULL,
  address varchar(200) DEFAULT NULL,  /*居住地*/
  grade varchar(50) DEFAULT NULL,  /*运动员等级*/
  years int(5),  /*运动年限*/
  dflx  varchar(60) DEFAULT NULL,  /*打法类型*/
  bscj  varchar(200) DEFAULT NULL, /*比赛成绩*/
  coachid varchar(20) DEFAULT NULL, 
  entrance_date varchar(20) DEFAULT NULL, /*入队年份*/
  retired varchar(2) DEFAULT NULL,  /*是否离队*/
  PRIMARY KEY (athleteid)
);

/*教练员信息*/
drop table coach;

CREATE TABLE coach (
  coachid varchar(20) NOT NULL,
  name varchar(20) NOT NULL,
  gender varchar(20) DEFAULT NULL,
  address varchar(20) DEFAULT NULL,
  grade varchar(20) DEFAULT NULL, /*教练员等级*/
  years int(5), /*执教年数*/
  PRIMARY KEY (coachid)
);

/*训练计划安排*/
drop table arrange;

CREATE TABLE arrange (
  id int(11) NOT NULL AUTO_INCREMENT,
  athleteid varchar(20) NOT NULL,
  timepoint varchar(20) NOT NULL,
  place varchar(20) NOT NULL,
  coachid varchar(20) NOT NULL,
  content varchar(100) NOT NULL,
  PRIMARY KEY (id)
);

/*击球力量原始数据表*/
drop table force_info;

CREATE TABLE force_info (
  id int(20) NOT NULL AUTO_INCREMENT,
  athleteid varchar(10) not NULL,
  actionid varchar(6) not NULL,
  testid   int(10) DEFAULT NULL,  /*测试序号*/
  testdate datetime DEFAULT NULL,
  ax float ,  /*三个方向的线加速度*/
  ay float ,
  az float ,
  anglex float , /*三个方向的角加速度*/
  angley float ,
  anglez float ,
  avx float ,   /*三个方向的线速度*/
  avy float ,
  avz float ,
  magnetismx float , /*三个方向的地磁*/
  magnetismy float ,
  magnetismz float ,
  temperature float ,
  mark int(5),
  PRIMARY KEY (id)
);

/*击球力量数据分析表*/
drop table analysis;

CREATE TABLE analysis (
  id int(11) NOT NULL AUTO_INCREMENT,
  athleteid varchar(10) not NULL,
  actionid varchar(6) not NULL,
  testid   int(10) ,  /*测试序号*/
  testdate datetime DEFAULT NULL,
  speedx float,       /*三个方向的线速度*/
  speedy float,
  speedz float,
  displacementx float,  /*三个方向的位移*/
  displacementy float,
  displacementz float,
  sportworkx float,      /*三个方向的功*/
  sportworky float,
  sportworkz float,
  mark int(5),
  PRIMARY KEY (id)
);

/*系统用户信息及权限管理表：采用现有系统的*/
drop table users;

CREATE TABLE users (
  userid varchar(20) NOT NULL,
  username varchar(20) NOT NULL,
  passWord varchar(20) DEFAULT NULL,
  role     varchar(10) DEFAULT NULL,
  PRIMARY KEY (userid)
);


二、动作捕捉数据

/*人体主要关节表*/

drop table joint;

CREATE TABLE joint (
  jointid varchar(20) NOT NULL,
  name    varchar(20) NOT NULL,
  memo    varchar(20) NOT NULL,
  PRIMARY KEY (jointid)
); 

/*动作捕捉原始数据*/

drop table motion_data;
CREATE TABLE motion_data (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  athleteid varchar(10) not NULL,
  actionid varchar(20) not NULL,
  testid   int(10),  /*测试序号*/
  testdate datetime DEFAULT NULL,
  frameno  int(10) not NULL,         /*帧编号*/
  hip_pos_x double ,     /*髋关节x,y,z三个方向的坐标*/
  hip_pos_y double ,
  hip_pos_z double ,
  hip_rot_x double ,     /*髋关节x,y,z三个方向的角度*/
  hip_rot_y double ,
  hip_rot_z double ,
  leftshoulder_pos_x double ,  /*左肩关节*/
  leftshoulder_pos_y double ,
  leftshoulder_pos_z double ,
  leftshoulder_rot_x double ,
  leftshoulder_rot_y double ,
  leftshoulder_rot_z double ,
  leftarm_pos_x double ,     /*左肘关节*/
  leftarm_pos_y double ,
  leftarm_pos_z double ,
  leftarm_rot_x double ,
  leftarm_rot_y double ,
  leftarm_rot_z double ,
  rightshoulder_pos_x double ,  /*右肩关节*/
  rightshoulder_pos_y double ,
  rightshoulder_pos_z double ,
  rightshoulder_rot_x double ,
  rightshoulder_rot_y double ,
  rightshoulder_rot_z double ,
  rightarm_pos_x double ,        /*右肘关节*/
  rightarm_pos_y double ,
  rightarm_pos_z double ,
  rightarm_rot_x double ,
  rightarm_rot_y double ,
  rightarm_rot_z double ,
  leftleg_pos_x double ,  /*左膝关节*/
  leftleg_pos_y double ,
  leftleg_pos_z double ,
  leftleg_rot_x double ,
  leftleg_rot_y double ,
  leftleg_rot_z double ,
  leftfoot_pos_x double ,  /*左踝关节*/
  leftfoot_pos_y double ,
  leftfoot_pos_z double ,
  leftfoot_rot_x double ,
  leftfoot_rot_y double ,
  leftfoot_rot_z double ,
  rightleg_pos_x double ,  /*右膝关节*/
  rightleg_pos_y double ,
  rightleg_pos_z double ,
  rightleg_rot_x double ,
  rightleg_rot_y double ,
  rightleg_rot_z double ,
  rightfoot_pos_x double , /*右踝关节*/
  rightfoot_pos_y double ,
  rightfoot_pos_z double ,
  rightfoot_rot_x double ,
  rightfoot_rot_y double ,
  rightfoot_rot_z double ,
  PRIMARY KEY (id)
);

/*个关节点发力顺序数据表：发力时的帧编号*/
drop table force_order;

CREATE TABLE force_order (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  athleteid varchar(10) not NULL,
  action varchar(20) not NULL,
  testid   int(10) ,  /*测试序号*/
  testdate datetime DEFAULT NULL,
  Hip         int(10),     /*髋关节*/
  LeftShoulder int(10) ,  /*左肩关节*/
  LeftArm     int(10) ,     /*左肘关节*/
  RightShoulder int(10) ,   /*右肩关节*/
  RightArm    int(10) ,     /*右肘关节*/
  LeftLeg     int(10) ,     /*左膝关节*/
  LeftFoot    int(10) ,     /*左踝关节*/
  RightLeg    int(10) ,     /*右膝关节*/
  RightFoot   int(10) ,     /*右踝关节*/
  PRIMARY KEY (id)
);


三、击球质量数据

/*击球质量数据表*/
drop table striking_effect;

CREATE TABLE striking_effect (
  id int(20) NOT NULL AUTO_INCREMENT,
  athleteid  varchar(10) not NULL,
  action   varchar(20) not NULL,
  testid   int(10) ,  /*测试序号*/
  testdate datetime DEFAULT NULL,
  spin	   double ,   /*转速*/
  speed	   double ,   /*球速*/
  point	   int ,   /*落点：-1:出界，0:下网, 1:上台，2:大区，3:小区*/
  PRIMARY KEY (id)
);

/*击球动作曲线与优秀运动员的相似度数据表：分总体相似度和三阶段相似度*/
drop table curve_fit;

CREATE TABLE curve_fit (
  id int(20) NOT NULL AUTO_INCREMENT,
  athleteid  varchar(10) not NULL,
  action   varchar(20) not NULL,
  testid   int(10) ,  /*测试序号*/
  testdate datetime DEFAULT NULL,
  jointid  varchar(20) NOT NULL,    /*关节编号*/
  pos_x	   double ,   /*x,y,z三个方向的关节位移曲线总体相似度*/
  pos_y	   double ,   
  pos_z	   double ,   
  rot_x	   double ,   /*x,y,z三个方向的关节角度曲线总体相似度*/
  rot_y	   double ,   
  rot_z	   double ,   
  pos_x_p1	   double ,   /*引拍阶段 x,y,z三个方向的位移曲线相似度*/
  pos_y_p1	   double ,   
  pos_z_p1	   double ,   
  pos_x_p2	   double ,   /*挥拍击球阶段 x,y,z三个方向的位移曲线相似度*/
  pos_y_p2	   double ,   
  pos_z_p2	   double ,   
  pos_x_p3	   double ,   /*还原阶段 x,y,z三个方向的位移曲线相似度*/
  pos_y_p3	   double ,   
  pos_z_p3	   double ,   
  rot_x_p1	   double ,   /*引拍阶段 x,y,z三个方向的角度曲线相似度*/
  rot_y_p1	   double ,   
  rot_z_p1	   double ,   
  rot_x_p2	   double ,   /*挥拍击球阶段 x,y,z三个方向的位角度线相似度*/
  rot_y_p2	   double ,   
  rot_z_p2	   double ,   
  rot_x_p3	   double ,   /*还原阶段 x,y,z三个方向的角度曲线相似度*/
  rot_y_p3	   double ,   
  rot_z_p3	   double ,   
  PRIMARY KEY (id)
);


/*击球动作曲线模型：存放优秀运动员某一击球动作过程各关节点的数据*/

drop table curve_model;

CREATE TABLE curve_model (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  actionid varchar(20) not NULL,
  frameno  int(10) not NULL,         /*帧编号*/
  hip_pos_x double ,     /*髋关节x,y,z三个方向的坐标*/
  hip_pos_y double ,
  hip_pos_z double ,
  hip_rot_x double ,     /*髋关节x,y,z三个方向的角度*/
  hip_rot_y double ,
  hip_rot_z double ,
  leftshoulder_pos_x double ,  /*左肩关节*/
  leftshoulder_pos_y double ,
  leftshoulder_pos_z double ,
  leftshoulder_rot_x double ,
  leftshoulder_rot_y double ,
  leftshoulder_rot_z double ,
  leftarm_pos_x double ,     /*左肘关节*/
  leftarm_pos_y double ,
  leftarm_pos_z double ,
  leftarm_rot_x double ,
  leftarm_rot_y double ,
  leftarm_rot_z double ,
  rightshoulder_pos_x double ,  /*右肩关节*/
  rightshoulder_pos_y double ,
  rightshoulder_pos_z double ,
  rightshoulder_rot_x double ,
  rightshoulder_rot_y double ,
  rightshoulder_rot_z double ,
  rightarm_pos_x double ,        /*右肘关节*/
  rightarm_pos_y double ,
  rightarm_pos_z double ,
  rightarm_rot_x double ,
  rightarm_rot_y double ,
  rightarm_rot_z double ,
  leftleg_pos_x double ,  /*左膝关节*/
  leftleg_pos_y double ,
  leftleg_pos_z double ,
  leftleg_rot_x double ,
  leftleg_rot_y double ,
  leftleg_rot_z double ,
  leftfoot_pos_x double ,  /*左踝关节*/
  leftfoot_pos_y double ,
  leftfoot_pos_z double ,
  leftfoot_rot_x double ,
  leftfoot_rot_y double ,
  leftfoot_rot_z double ,
  rightleg_pos_x double ,  /*右膝关节*/
  rightleg_pos_y double ,
  rightleg_pos_z double ,
  rightleg_rot_x double ,
  rightleg_rot_y double ,
  rightleg_rot_z double ,
  rightfoot_pos_x double , /*右踝关节*/
  rightfoot_pos_y double ,
  rightfoot_pos_z double ,
  rightfoot_rot_x double ,
  rightfoot_rot_y double ,
  rightfoot_rot_z double ,
  PRIMARY KEY (id)
);

/*训练强度数据表：心率监控*/
drop table hrate_info;

CREATE TABLE hrate_info (
  id int(20) NOT NULL AUTO_INCREMENT,
  athleteid varchar(10) not NULL,
  actionid varchar(6) not NULL,
  testid   int(10) DEFAULT NULL,  /*测试序号*/
  testdate datetime DEFAULT NULL,
  hr_start float ,  /*训练开始心率*/
  hr_end   float ,  /*训练结束心率*/
  hr_min   float ,  /*心率最小值*/
  hr_avg   float ,  /*心率平均值*/
  hr_max   float ,  /*心率最大值*/
  PRIMARY KEY (id)
);

/*生理生化指标监控*/
drop table physiology_test;

CREATE TABLE physiology_test (
  id int(11) NOT NULL AUTO_INCREMENT,
  date date DEFAULT NULL,
  gaotong double DEFAULT NULL,
  pizhichun double DEFAULT NULL,
  niaosudan double DEFAULT NULL,
  jisuanjimei double DEFAULT NULL,
  tc double DEFAULT NULL,           /*总胆固醇*/
  yichang varchar(50) DEFAULT NULL, /*异常*/
  athlete_id int(11) NOT NULL,
  PRIMARY KEY (id)
  );

/*比赛成绩*/
drop table performance;

CREATE TABLE performance(
  id int(11) NOT NULL AUTO_INCREMENT,
  athlete_id int(11) NOT NULL,
  rival      varchar(50) DEFAULT NULL, /*对手名称*/
  date date DEFAULT NULL,
  mingcheng varchar(50) DEFAULT NULL,
  xiangmu int(11) NOT NULL,  /*1：单打，2：双打*/
  result    varchar(10) NOT NULL,      /*比赛结果：总比分*/
  r1        varchar(10) NOT NULL,      /*第1局比分*/
  r2        varchar(10) NOT NULL,      /*第2局比分*/
  r3        varchar(10) NOT NULL,      /*第3局比分*/
  r4        varchar(10) NOT NULL,      /*第4局比分*/
  r5        varchar(10) NOT NULL,      /*第5局比分*/
  r6        varchar(10) NOT NULL,      /*第6局比分*/
  r7        varchar(10) NOT NULL,      /*第7局比分*/
  PRIMARY KEY (id)
  );