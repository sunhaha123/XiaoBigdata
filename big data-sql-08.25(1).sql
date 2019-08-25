Ŀ¼�ṹ

һ��Ŀ¼
   ��1��������Ϣ
        ����Ŀ¼���˶�Ա��Ϣ������Ա��Ϣ����������������Ҫ�ؽڵ�
   ��2��ѵ������
	����Ŀ¼��ѵ���ƻ���ѵ��ǿ�ȡ���������ָ�ꡢ�����ɼ�
   ��3��������׽
	����Ŀ¼��������׽ԭʼ���ݡ��ؽڵ㷢��˳�򡢶�������ģ��
   ��4����������
	����Ŀ¼����������ԭʼ����
   ��5����������
	����Ŀ¼��������������
   ��6�������ݷ��������ӻ�
	�����������ƶȷ����������������ݷ������������������Է���������Ч�������Է������������������Ч��������Է���
   ��7��ϵͳ����


һ��������������

/*������*/
drop table action;

CREATE TABLE action (
  actionid int(6) NOT NULL,
  name    varchar(20) NOT NULL,
  memo    varchar(20) NOT NULL,
  PRIMARY KEY (actionid)
); 

/*�˶�Ա������Ϣ��*/
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
  address varchar(200) DEFAULT NULL,  /*��ס��*/
  grade varchar(50) DEFAULT NULL,  /*�˶�Ա�ȼ�*/
  years int(5),  /*�˶�����*/
  dflx  varchar(60) DEFAULT NULL,  /*������*/
  bscj  varchar(200) DEFAULT NULL, /*�����ɼ�*/
  coachid varchar(20) DEFAULT NULL, 
  entrance_date varchar(20) DEFAULT NULL, /*������*/
  retired varchar(2) DEFAULT NULL,  /*�Ƿ����*/
  PRIMARY KEY (athleteid)
);

/*����Ա��Ϣ*/
drop table coach;

CREATE TABLE coach (
  coachid varchar(20) NOT NULL,
  name varchar(20) NOT NULL,
  gender varchar(20) DEFAULT NULL,
  address varchar(20) DEFAULT NULL,
  grade varchar(20) DEFAULT NULL, /*����Ա�ȼ�*/
  years int(5), /*ִ������*/
  PRIMARY KEY (coachid)
);

/*ѵ���ƻ�����*/
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

/*��������ԭʼ���ݱ�*/
drop table force_info;

CREATE TABLE force_info (
  id int(20) NOT NULL AUTO_INCREMENT,
  athleteid varchar(10) not NULL,
  actionid varchar(6) not NULL,
  testid   int(10) DEFAULT NULL,  /*�������*/
  testdate datetime DEFAULT NULL,
  ax float ,  /*����������߼��ٶ�*/
  ay float ,
  az float ,
  anglex float , /*��������ĽǼ��ٶ�*/
  angley float ,
  anglez float ,
  avx float ,   /*������������ٶ�*/
  avy float ,
  avz float ,
  magnetismx float , /*��������ĵش�*/
  magnetismy float ,
  magnetismz float ,
  temperature float ,
  mark int(5),
  PRIMARY KEY (id)
);

/*�����������ݷ�����*/
drop table analysis;

CREATE TABLE analysis (
  id int(11) NOT NULL AUTO_INCREMENT,
  athleteid varchar(10) not NULL,
  actionid varchar(6) not NULL,
  testid   int(10) ,  /*�������*/
  testdate datetime DEFAULT NULL,
  speedx float,       /*������������ٶ�*/
  speedy float,
  speedz float,
  displacementx float,  /*���������λ��*/
  displacementy float,
  displacementz float,
  sportworkx float,      /*��������Ĺ�*/
  sportworky float,
  sportworkz float,
  mark int(5),
  PRIMARY KEY (id)
);

/*ϵͳ�û���Ϣ��Ȩ�޹������������ϵͳ��*/
drop table users;

CREATE TABLE users (
  userid varchar(20) NOT NULL,
  username varchar(20) NOT NULL,
  passWord varchar(20) DEFAULT NULL,
  role     varchar(10) DEFAULT NULL,
  PRIMARY KEY (userid)
);


����������׽����

/*������Ҫ�ؽڱ�*/

drop table joint;

CREATE TABLE joint (
  jointid varchar(20) NOT NULL,
  name    varchar(20) NOT NULL,
  memo    varchar(20) NOT NULL,
  PRIMARY KEY (jointid)
); 

/*������׽ԭʼ����*/

drop table motion_data;
CREATE TABLE motion_data (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  athleteid varchar(10) not NULL,
  actionid varchar(20) not NULL,
  testid   int(10),  /*�������*/
  testdate datetime DEFAULT NULL,
  frameno  int(10) not NULL,         /*֡���*/
  hip_pos_x double ,     /*�Źؽ�x,y,z�������������*/
  hip_pos_y double ,
  hip_pos_z double ,
  hip_rot_x double ,     /*�Źؽ�x,y,z��������ĽǶ�*/
  hip_rot_y double ,
  hip_rot_z double ,
  leftshoulder_pos_x double ,  /*���ؽ�*/
  leftshoulder_pos_y double ,
  leftshoulder_pos_z double ,
  leftshoulder_rot_x double ,
  leftshoulder_rot_y double ,
  leftshoulder_rot_z double ,
  leftarm_pos_x double ,     /*����ؽ�*/
  leftarm_pos_y double ,
  leftarm_pos_z double ,
  leftarm_rot_x double ,
  leftarm_rot_y double ,
  leftarm_rot_z double ,
  rightshoulder_pos_x double ,  /*�Ҽ�ؽ�*/
  rightshoulder_pos_y double ,
  rightshoulder_pos_z double ,
  rightshoulder_rot_x double ,
  rightshoulder_rot_y double ,
  rightshoulder_rot_z double ,
  rightarm_pos_x double ,        /*����ؽ�*/
  rightarm_pos_y double ,
  rightarm_pos_z double ,
  rightarm_rot_x double ,
  rightarm_rot_y double ,
  rightarm_rot_z double ,
  leftleg_pos_x double ,  /*��ϥ�ؽ�*/
  leftleg_pos_y double ,
  leftleg_pos_z double ,
  leftleg_rot_x double ,
  leftleg_rot_y double ,
  leftleg_rot_z double ,
  leftfoot_pos_x double ,  /*���׹ؽ�*/
  leftfoot_pos_y double ,
  leftfoot_pos_z double ,
  leftfoot_rot_x double ,
  leftfoot_rot_y double ,
  leftfoot_rot_z double ,
  rightleg_pos_x double ,  /*��ϥ�ؽ�*/
  rightleg_pos_y double ,
  rightleg_pos_z double ,
  rightleg_rot_x double ,
  rightleg_rot_y double ,
  rightleg_rot_z double ,
  rightfoot_pos_x double , /*���׹ؽ�*/
  rightfoot_pos_y double ,
  rightfoot_pos_z double ,
  rightfoot_rot_x double ,
  rightfoot_rot_y double ,
  rightfoot_rot_z double ,
  PRIMARY KEY (id)
);

/*���ؽڵ㷢��˳�����ݱ�����ʱ��֡���*/
drop table force_order;

CREATE TABLE force_order (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  athleteid varchar(10) not NULL,
  action varchar(20) not NULL,
  testid   int(10) ,  /*�������*/
  testdate datetime DEFAULT NULL,
  Hip         int(10),     /*�Źؽ�*/
  LeftShoulder int(10) ,  /*���ؽ�*/
  LeftArm     int(10) ,     /*����ؽ�*/
  RightShoulder int(10) ,   /*�Ҽ�ؽ�*/
  RightArm    int(10) ,     /*����ؽ�*/
  LeftLeg     int(10) ,     /*��ϥ�ؽ�*/
  LeftFoot    int(10) ,     /*���׹ؽ�*/
  RightLeg    int(10) ,     /*��ϥ�ؽ�*/
  RightFoot   int(10) ,     /*���׹ؽ�*/
  PRIMARY KEY (id)
);


����������������

/*�����������ݱ�*/
drop table striking_effect;

CREATE TABLE striking_effect (
  id int(20) NOT NULL AUTO_INCREMENT,
  athleteid  varchar(10) not NULL,
  action   varchar(20) not NULL,
  testid   int(10) ,  /*�������*/
  testdate datetime DEFAULT NULL,
  spin	   double ,   /*ת��*/
  speed	   double ,   /*����*/
  point	   int ,   /*��㣺-1:���磬0:����, 1:��̨��2:������3:С��*/
  PRIMARY KEY (id)
);

/*�����������������˶�Ա�����ƶ����ݱ����������ƶȺ����׶����ƶ�*/
drop table curve_fit;

CREATE TABLE curve_fit (
  id int(20) NOT NULL AUTO_INCREMENT,
  athleteid  varchar(10) not NULL,
  action   varchar(20) not NULL,
  testid   int(10) ,  /*�������*/
  testdate datetime DEFAULT NULL,
  jointid  varchar(20) NOT NULL,    /*�ؽڱ��*/
  pos_x	   double ,   /*x,y,z��������Ĺؽ�λ�������������ƶ�*/
  pos_y	   double ,   
  pos_z	   double ,   
  rot_x	   double ,   /*x,y,z��������ĹؽڽǶ������������ƶ�*/
  rot_y	   double ,   
  rot_z	   double ,   
  pos_x_p1	   double ,   /*���Ľ׶� x,y,z���������λ���������ƶ�*/
  pos_y_p1	   double ,   
  pos_z_p1	   double ,   
  pos_x_p2	   double ,   /*���Ļ���׶� x,y,z���������λ���������ƶ�*/
  pos_y_p2	   double ,   
  pos_z_p2	   double ,   
  pos_x_p3	   double ,   /*��ԭ�׶� x,y,z���������λ���������ƶ�*/
  pos_y_p3	   double ,   
  pos_z_p3	   double ,   
  rot_x_p1	   double ,   /*���Ľ׶� x,y,z��������ĽǶ��������ƶ�*/
  rot_y_p1	   double ,   
  rot_z_p1	   double ,   
  rot_x_p2	   double ,   /*���Ļ���׶� x,y,z���������λ�Ƕ������ƶ�*/
  rot_y_p2	   double ,   
  rot_z_p2	   double ,   
  rot_x_p3	   double ,   /*��ԭ�׶� x,y,z��������ĽǶ��������ƶ�*/
  rot_y_p3	   double ,   
  rot_z_p3	   double ,   
  PRIMARY KEY (id)
);


/*����������ģ�ͣ���������˶�Աĳһ���������̸��ؽڵ������*/

drop table curve_model;

CREATE TABLE curve_model (
  id bigint(20) NOT NULL AUTO_INCREMENT,
  actionid varchar(20) not NULL,
  frameno  int(10) not NULL,         /*֡���*/
  hip_pos_x double ,     /*�Źؽ�x,y,z�������������*/
  hip_pos_y double ,
  hip_pos_z double ,
  hip_rot_x double ,     /*�Źؽ�x,y,z��������ĽǶ�*/
  hip_rot_y double ,
  hip_rot_z double ,
  leftshoulder_pos_x double ,  /*���ؽ�*/
  leftshoulder_pos_y double ,
  leftshoulder_pos_z double ,
  leftshoulder_rot_x double ,
  leftshoulder_rot_y double ,
  leftshoulder_rot_z double ,
  leftarm_pos_x double ,     /*����ؽ�*/
  leftarm_pos_y double ,
  leftarm_pos_z double ,
  leftarm_rot_x double ,
  leftarm_rot_y double ,
  leftarm_rot_z double ,
  rightshoulder_pos_x double ,  /*�Ҽ�ؽ�*/
  rightshoulder_pos_y double ,
  rightshoulder_pos_z double ,
  rightshoulder_rot_x double ,
  rightshoulder_rot_y double ,
  rightshoulder_rot_z double ,
  rightarm_pos_x double ,        /*����ؽ�*/
  rightarm_pos_y double ,
  rightarm_pos_z double ,
  rightarm_rot_x double ,
  rightarm_rot_y double ,
  rightarm_rot_z double ,
  leftleg_pos_x double ,  /*��ϥ�ؽ�*/
  leftleg_pos_y double ,
  leftleg_pos_z double ,
  leftleg_rot_x double ,
  leftleg_rot_y double ,
  leftleg_rot_z double ,
  leftfoot_pos_x double ,  /*���׹ؽ�*/
  leftfoot_pos_y double ,
  leftfoot_pos_z double ,
  leftfoot_rot_x double ,
  leftfoot_rot_y double ,
  leftfoot_rot_z double ,
  rightleg_pos_x double ,  /*��ϥ�ؽ�*/
  rightleg_pos_y double ,
  rightleg_pos_z double ,
  rightleg_rot_x double ,
  rightleg_rot_y double ,
  rightleg_rot_z double ,
  rightfoot_pos_x double , /*���׹ؽ�*/
  rightfoot_pos_y double ,
  rightfoot_pos_z double ,
  rightfoot_rot_x double ,
  rightfoot_rot_y double ,
  rightfoot_rot_z double ,
  PRIMARY KEY (id)
);

/*ѵ��ǿ�����ݱ����ʼ��*/
drop table hrate_info;

CREATE TABLE hrate_info (
  id int(20) NOT NULL AUTO_INCREMENT,
  athleteid varchar(10) not NULL,
  actionid varchar(6) not NULL,
  testid   int(10) DEFAULT NULL,  /*�������*/
  testdate datetime DEFAULT NULL,
  hr_start float ,  /*ѵ����ʼ����*/
  hr_end   float ,  /*ѵ����������*/
  hr_min   float ,  /*������Сֵ*/
  hr_avg   float ,  /*����ƽ��ֵ*/
  hr_max   float ,  /*�������ֵ*/
  PRIMARY KEY (id)
);

/*��������ָ����*/
drop table physiology_test;

CREATE TABLE physiology_test (
  id int(11) NOT NULL AUTO_INCREMENT,
  date date DEFAULT NULL,
  gaotong double DEFAULT NULL,
  pizhichun double DEFAULT NULL,
  niaosudan double DEFAULT NULL,
  jisuanjimei double DEFAULT NULL,
  tc double DEFAULT NULL,           /*�ܵ��̴�*/
  yichang varchar(50) DEFAULT NULL, /*�쳣*/
  athlete_id int(11) NOT NULL,
  PRIMARY KEY (id)
  );

/*�����ɼ�*/
drop table performance;

CREATE TABLE performance(
  id int(11) NOT NULL AUTO_INCREMENT,
  athlete_id int(11) NOT NULL,
  rival      varchar(50) DEFAULT NULL, /*��������*/
  date date DEFAULT NULL,
  mingcheng varchar(50) DEFAULT NULL,
  xiangmu int(11) NOT NULL,  /*1������2��˫��*/
  result    varchar(10) NOT NULL,      /*����������ܱȷ�*/
  r1        varchar(10) NOT NULL,      /*��1�ֱȷ�*/
  r2        varchar(10) NOT NULL,      /*��2�ֱȷ�*/
  r3        varchar(10) NOT NULL,      /*��3�ֱȷ�*/
  r4        varchar(10) NOT NULL,      /*��4�ֱȷ�*/
  r5        varchar(10) NOT NULL,      /*��5�ֱȷ�*/
  r6        varchar(10) NOT NULL,      /*��6�ֱȷ�*/
  r7        varchar(10) NOT NULL,      /*��7�ֱȷ�*/
  PRIMARY KEY (id)
  );