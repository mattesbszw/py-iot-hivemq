drop table if exists iot_devices;

create table iot_devices (
	id integer auto_increment not null,
	device_name varchar(127) not null,
	mqtt_topic varchar(255) not null,
	primary key (id)
);

insert into iot_devices (device_name, mqtt_topic)
values 
 ('Sensors General', 'bszw/mat/sensors/general'),
 ('DHT22 Temperature', 'bszw/mat/sensors/dht/temp'),
 ('DHT22 Humdidty', 'bszw/mat/sensors/dht/hum'),
 ('DS18B20 Temperature', 'bszw/mat/sensors/ds/temp'),
 ('Reed Contact Garage', 'bszw/mat/sensors/reed/garage'),
 ('Reed Window Kitchen', 'bszw/mat/sensors/reed/kitchen'),
 ('Shelly1 Office Status', 'bszw/mat/sensors/shelly/office/status'),
 ('Shelly1 Office Power Consumsation', 'bszw/mat/sensors/shelly/office/power');

drop table if exists iot_sensor_values;

create table iot_sensor_values (
	id integer auto_increment not null,
	device_id integer not null,
	value double not null default 0,
	timestamp datetime not null,
	primary key(id),
	foreign key(device_id) references iot_devices(id)
);