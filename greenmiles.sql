-- Adminer 4.7.7 PostgreSQL dump

DROP TABLE IF EXISTS "auth_group";
DROP SEQUENCE IF EXISTS auth_group_id_seq;
CREATE SEQUENCE auth_group_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."auth_group" (
    "id" integer DEFAULT nextval('auth_group_id_seq') NOT NULL,
    "name" character varying(80) NOT NULL,
    CONSTRAINT "auth_group_name_key" UNIQUE ("name"),
    CONSTRAINT "auth_group_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "auth_group_name_a6ea08ec_like" ON "public"."auth_group" USING btree ("name");


DROP TABLE IF EXISTS "auth_group_permissions";
DROP SEQUENCE IF EXISTS auth_group_permissions_id_seq;
CREATE SEQUENCE auth_group_permissions_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."auth_group_permissions" (
    "id" integer DEFAULT nextval('auth_group_permissions_id_seq') NOT NULL,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL,
    CONSTRAINT "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" UNIQUE ("group_id", "permission_id"),
    CONSTRAINT "auth_group_permissions_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE,
    CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE
) WITH (oids = false);

CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "public"."auth_group_permissions" USING btree ("group_id");

CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "public"."auth_group_permissions" USING btree ("permission_id");


DROP TABLE IF EXISTS "auth_permission";
DROP SEQUENCE IF EXISTS auth_permission_id_seq;
CREATE SEQUENCE auth_permission_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."auth_permission" (
    "id" integer DEFAULT nextval('auth_permission_id_seq') NOT NULL,
    "name" character varying(255) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" character varying(100) NOT NULL,
    CONSTRAINT "auth_permission_content_type_id_codename_01ab375a_uniq" UNIQUE ("content_type_id", "codename"),
    CONSTRAINT "auth_permission_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE
) WITH (oids = false);

CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "public"."auth_permission" USING btree ("content_type_id");

INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES
(1,	'Can add log entry',	1,	'add_logentry'),
(2,	'Can change log entry',	1,	'change_logentry'),
(3,	'Can delete log entry',	1,	'delete_logentry'),
(4,	'Can add permission',	2,	'add_permission'),
(5,	'Can change permission',	2,	'change_permission'),
(6,	'Can delete permission',	2,	'delete_permission'),
(7,	'Can add group',	3,	'add_group'),
(8,	'Can change group',	3,	'change_group'),
(9,	'Can delete group',	3,	'delete_group'),
(10,	'Can add user',	4,	'add_user'),
(11,	'Can change user',	4,	'change_user'),
(12,	'Can delete user',	4,	'delete_user'),
(13,	'Can add content type',	5,	'add_contenttype'),
(14,	'Can change content type',	5,	'change_contenttype'),
(15,	'Can delete content type',	5,	'delete_contenttype'),
(16,	'Can add session',	6,	'add_session'),
(17,	'Can change session',	6,	'change_session'),
(18,	'Can delete session',	6,	'delete_session');

DROP TABLE IF EXISTS "auth_user";
DROP SEQUENCE IF EXISTS auth_user_id_seq;
CREATE SEQUENCE auth_user_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."auth_user" (
    "id" integer DEFAULT nextval('auth_user_id_seq') NOT NULL,
    "password" character varying(128) NOT NULL,
    "last_login" timestamptz,
    "is_superuser" boolean NOT NULL,
    "username" character varying(150) NOT NULL,
    "first_name" character varying(30) NOT NULL,
    "last_name" character varying(150) NOT NULL,
    "email" character varying(254) NOT NULL,
    "is_staff" boolean NOT NULL,
    "is_active" boolean NOT NULL,
    "date_joined" timestamptz NOT NULL,
    CONSTRAINT "auth_user_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "auth_user_username_key" UNIQUE ("username")
) WITH (oids = false);

CREATE INDEX "auth_user_username_6821ab7c_like" ON "public"."auth_user" USING btree ("username");


DROP TABLE IF EXISTS "auth_user_groups";
DROP SEQUENCE IF EXISTS auth_user_groups_id_seq;
CREATE SEQUENCE auth_user_groups_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."auth_user_groups" (
    "id" integer DEFAULT nextval('auth_user_groups_id_seq') NOT NULL,
    "user_id" integer NOT NULL,
    "group_id" integer NOT NULL,
    CONSTRAINT "auth_user_groups_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "auth_user_groups_user_id_group_id_94350c0c_uniq" UNIQUE ("user_id", "group_id"),
    CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE,
    CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE
) WITH (oids = false);

CREATE INDEX "auth_user_groups_group_id_97559544" ON "public"."auth_user_groups" USING btree ("group_id");

CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "public"."auth_user_groups" USING btree ("user_id");


DROP TABLE IF EXISTS "auth_user_user_permissions";
DROP SEQUENCE IF EXISTS auth_user_user_permissions_id_seq;
CREATE SEQUENCE auth_user_user_permissions_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."auth_user_user_permissions" (
    "id" integer DEFAULT nextval('auth_user_user_permissions_id_seq') NOT NULL,
    "user_id" integer NOT NULL,
    "permission_id" integer NOT NULL,
    CONSTRAINT "auth_user_user_permissions_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" UNIQUE ("user_id", "permission_id"),
    CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE,
    CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE
) WITH (oids = false);

CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "public"."auth_user_user_permissions" USING btree ("permission_id");

CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "public"."auth_user_user_permissions" USING btree ("user_id");


DROP TABLE IF EXISTS "badges";
DROP SEQUENCE IF EXISTS badges_id_seq;
CREATE SEQUENCE badges_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."badges" (
    "id" integer DEFAULT nextval('badges_id_seq') NOT NULL,
    "created_at" timestamptz NOT NULL,
    "challenge_id" integer,
    "user_id" integer,
    CONSTRAINT "badges_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "badges_challenge_id_b2d274c9_fk_challenges_id" FOREIGN KEY (challenge_id) REFERENCES challenges(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE
) WITH (oids = false);

CREATE INDEX "badges_challenge_id_b2d274c9" ON "public"."badges" USING btree ("challenge_id");


DROP TABLE IF EXISTS "challenges";
DROP SEQUENCE IF EXISTS challenges_id_seq;
CREATE SEQUENCE challenges_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."challenges" (
    "id" integer DEFAULT nextval('challenges_id_seq') NOT NULL,
    "title" character varying(150),
    "unit" character varying(50),
    "description" text,
    "target" integer,
    "challenge_type" character varying(32),
    "due_date" timestamptz NOT NULL,
    "status" character varying(32),
    "created_at" timestamptz NOT NULL,
    "thumbnail_active" text,
    "thumbnail_inactive" text,
    CONSTRAINT "challenges_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "django_admin_log";
DROP SEQUENCE IF EXISTS django_admin_log_id_seq;
CREATE SEQUENCE django_admin_log_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."django_admin_log" (
    "id" integer DEFAULT nextval('django_admin_log_id_seq') NOT NULL,
    "action_time" timestamptz NOT NULL,
    "object_id" text,
    "object_repr" character varying(200) NOT NULL,
    "action_flag" smallint NOT NULL,
    "change_message" text NOT NULL,
    "content_type_id" integer,
    "user_id" integer NOT NULL,
    CONSTRAINT "django_admin_log_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE,
    CONSTRAINT "django_admin_log_user_id_c564eba6_fk" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE
) WITH (oids = false);

CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "public"."django_admin_log" USING btree ("content_type_id");

CREATE INDEX "django_admin_log_user_id_c564eba6" ON "public"."django_admin_log" USING btree ("user_id");


DROP TABLE IF EXISTS "django_content_type";
DROP SEQUENCE IF EXISTS django_content_type_id_seq;
CREATE SEQUENCE django_content_type_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."django_content_type" (
    "id" integer DEFAULT nextval('django_content_type_id_seq') NOT NULL,
    "app_label" character varying(100) NOT NULL,
    "model" character varying(100) NOT NULL,
    CONSTRAINT "django_content_type_app_label_model_76bd3d3b_uniq" UNIQUE ("app_label", "model"),
    CONSTRAINT "django_content_type_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "django_content_type" ("id", "app_label", "model") VALUES
(1,	'admin',	'logentry'),
(2,	'auth',	'permission'),
(3,	'auth',	'group'),
(4,	'auth',	'user'),
(5,	'contenttypes',	'contenttype'),
(6,	'sessions',	'session');

DROP TABLE IF EXISTS "django_migrations";
DROP SEQUENCE IF EXISTS django_migrations_id_seq;
CREATE SEQUENCE django_migrations_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."django_migrations" (
    "id" integer DEFAULT nextval('django_migrations_id_seq') NOT NULL,
    "app" character varying(255) NOT NULL,
    "name" character varying(255) NOT NULL,
    "applied" timestamptz NOT NULL,
    CONSTRAINT "django_migrations_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES
(1,	'contenttypes',	'0001_initial',	'2022-06-12 12:03:46.175963+07'),
(2,	'auth',	'0001_initial',	'2022-06-12 12:03:51.44266+07'),
(3,	'admin',	'0001_initial',	'2022-06-12 12:03:53.241884+07'),
(4,	'admin',	'0002_logentry_remove_auto_add',	'2022-06-12 12:03:53.601496+07'),
(5,	'contenttypes',	'0002_remove_content_type_name',	'2022-06-12 12:03:55.063361+07'),
(6,	'auth',	'0002_alter_permission_name_max_length',	'2022-06-12 12:03:55.720688+07'),
(7,	'auth',	'0003_alter_user_email_max_length',	'2022-06-12 12:03:56.841947+07'),
(8,	'auth',	'0004_alter_user_username_opts',	'2022-06-12 12:03:57.233189+07'),
(9,	'auth',	'0005_alter_user_last_login_null',	'2022-06-12 12:03:58.296082+07'),
(10,	'auth',	'0006_require_contenttypes_0002',	'2022-06-12 12:03:58.681813+07'),
(11,	'auth',	'0007_alter_validators_add_error_messages',	'2022-06-12 12:03:59.071761+07'),
(12,	'auth',	'0008_alter_user_username_max_length',	'2022-06-12 12:04:00.760883+07'),
(13,	'auth',	'0009_alter_user_last_name_max_length',	'2022-06-12 12:04:02.641534+07'),
(14,	'sessions',	'0001_initial',	'2022-06-12 12:04:05.576809+07'),
(15,	'rest_admin',	'0001_initial',	'2022-06-12 12:11:39.802834+07'),
(16,	'rest_admin',	'0002_profile_user_id',	'2022-06-12 14:39:31.024662+07'),
(17,	'rest_admin',	'0003_auto_20220612_1548',	'2022-06-12 15:48:23.269686+07'),
(18,	'rest_admin',	'0004_auto_20220612_1556',	'2022-06-12 15:56:42.679623+07'),
(19,	'rest_admin',	'0005_auto_20220612_1558',	'2022-06-12 15:58:43.43035+07'),
(20,	'rest_admin',	'0006_auto_20220612_1731',	'2022-06-12 17:31:08.949741+07'),
(21,	'rest_admin',	'0007_auto_20220612_1732',	'2022-06-12 17:32:24.182235+07'),
(22,	'rest_admin',	'0008_auto_20220612_1739',	'2022-06-12 17:39:22.539867+07');

DROP TABLE IF EXISTS "django_session";
CREATE TABLE "public"."django_session" (
    "session_key" character varying(40) NOT NULL,
    "session_data" text NOT NULL,
    "expire_date" timestamptz NOT NULL,
    CONSTRAINT "django_session_pkey" PRIMARY KEY ("session_key")
) WITH (oids = false);

CREATE INDEX "django_session_expire_date_a5c62663" ON "public"."django_session" USING btree ("expire_date");

CREATE INDEX "django_session_session_key_c0390e0f_like" ON "public"."django_session" USING btree ("session_key");


DROP TABLE IF EXISTS "journey_details";
DROP SEQUENCE IF EXISTS journey_details_id_seq;
CREATE SEQUENCE journey_details_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."journey_details" (
    "id" integer DEFAULT nextval('journey_details_id_seq') NOT NULL,
    "start_point" character varying(150),
    "end_point" character varying(150),
    "distance" numeric(15,2),
    "emission" numeric(15,2),
    "order" integer,
    "lat_start_point" numeric(12,6),
    "long_start_point" numeric(12,6),
    "lat_end_point" numeric(12,6),
    "long_end_point" numeric(12,6),
    "vehicle_type" character varying(32),
    "created_at" timestamptz NOT NULL,
    "journey_id" integer,
    CONSTRAINT "journey_details_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "journey_details_journey_id_4ab2eae9_fk_journeys_id" FOREIGN KEY (journey_id) REFERENCES journeys(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE
) WITH (oids = false);

CREATE INDEX "journey_details_journey_id_4ab2eae9" ON "public"."journey_details" USING btree ("journey_id");

INSERT INTO "journey_details" ("id", "start_point", "end_point", "distance", "emission", "order", "lat_start_point", "long_start_point", "lat_end_point", "long_end_point", "vehicle_type", "created_at", "journey_id") VALUES
(2,	'Green Hills Residence A8',	'Bekasi Station',	2.00,	0.30,	1,	NULL,	NULL,	NULL,	NULL,	'GrabBike',	'2022-06-12 17:16:07.384226+07',	2),
(3,	'Bekasi Station',	'Sudirman Station',	40.00,	1.60,	2,	NULL,	NULL,	NULL,	NULL,	'Train',	'2022-06-12 17:16:07.384226+07',	2),
(4,	'Sudirman Station',	'SCBD District 8',	2.00,	0.54,	3,	NULL,	NULL,	NULL,	NULL,	'GrabCar',	'2022-06-12 17:16:07.384226+07',	2),
(5,	'Green Hills Residence A8',	'SCBD District 8',	44.00,	10.00,	4,	NULL,	NULL,	NULL,	NULL,	'Car',	'2022-06-12 17:16:07.384226+07',	2);

DROP TABLE IF EXISTS "journeys";
DROP SEQUENCE IF EXISTS journeys_id_seq;
CREATE SEQUENCE journeys_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."journeys" (
    "id" integer DEFAULT nextval('journeys_id_seq') NOT NULL,
    "title" character varying(150),
    "start_point" character varying(150),
    "end_point" character varying(150),
    "distance" numeric(15,2),
    "miles" numeric(15,2),
    "date" date,
    "type" character varying(32),
    "emission_occured" numeric(15,2),
    "emission_actual" numeric(15,2),
    "emission_reduced" numeric(15,2),
    "journey_map" text,
    "lat_start_point" numeric(12,6),
    "long_start_point" numeric(12,6),
    "lat_end_point" numeric(12,6),
    "long_end_point" numeric(12,6),
    "created_at" timestamptz NOT NULL,
    "user_id" integer,
    CONSTRAINT "journeys_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "journeys" ("id", "title", "start_point", "end_point", "distance", "miles", "date", "type", "emission_occured", "emission_actual", "emission_reduced", "journey_map", "lat_start_point", "long_start_point", "lat_end_point", "long_end_point", "created_at", "user_id") VALUES
(2,	'Trip to SCBD District 8',	'Green Hills Residence A8',	'SCBD District 8',	44.00,	7.80,	'2022-06-10',	'MRT',	2.40,	9.80,	7.40,	'https://storage.googleapis.com/greenmiles/map1.png',	-6.280722,	107.037739,	-6.224590,	106.808897,	'2022-06-12 15:58:45.01185+07',	1000),
(3,	'Trip to SCBD District 8',	'Green Hills Residence A8',	'SCBD District 8',	44.00,	7.80,	'2022-06-10',	'Train',	2.40,	9.80,	7.40,	'https://storage.googleapis.com/greenmiles/map1.png',	-6.280722,	107.037739,	-6.224590,	106.808897,	'2022-06-12 15:58:45.01185+07',	1000),
(4,	'Trip to SCBD District 8',	'Green Hills Residence A8',	'SCBD District 8',	44.00,	7.80,	'2022-06-10',	'Bus',	2.40,	9.80,	7.40,	'https://storage.googleapis.com/greenmiles/map1.png',	-6.280722,	107.037739,	-6.224590,	106.808897,	'2022-06-12 15:58:45.01185+07',	1000);

DROP TABLE IF EXISTS "profiles";
DROP SEQUENCE IF EXISTS profiles_id_seq;
CREATE SEQUENCE profiles_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."profiles" (
    "id" integer DEFAULT nextval('profiles_id_seq') NOT NULL,
    "name" character varying(150),
    "level" character varying(150),
    "miles" numeric(15,2),
    "journeys" integer,
    "distance" numeric(15,2),
    "created_at" timestamptz NOT NULL,
    "user_id" character varying(150),
    CONSTRAINT "profiles_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "profiles" ("id", "name", "level", "miles", "journeys", "distance", "created_at", "user_id") VALUES
(1000,	'Diqfan Haris Imaman',	'Green Knight',	3120.00,	30,	690.00,	'2022-06-12 14:37:56.811052+07',	'1000');

DROP TABLE IF EXISTS "rewards";
DROP SEQUENCE IF EXISTS rewards_id_seq;
CREATE SEQUENCE rewards_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."rewards" (
    "id" integer DEFAULT nextval('rewards_id_seq') NOT NULL,
    "status" character varying(32),
    "created_at" timestamptz NOT NULL,
    "user_id" integer,
    "voucher_id" integer,
    CONSTRAINT "rewards_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "rewards_user_id_fe457069_fk_profiles_id" FOREIGN KEY (user_id) REFERENCES profiles(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE,
    CONSTRAINT "rewards_voucher_id_16d0274e_fk_vouchers_id" FOREIGN KEY (voucher_id) REFERENCES vouchers(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE
) WITH (oids = false);

CREATE INDEX "rewards_user_id_fe457069" ON "public"."rewards" USING btree ("user_id");

CREATE INDEX "rewards_voucher_id_16d0274e" ON "public"."rewards" USING btree ("voucher_id");

INSERT INTO "rewards" ("id", "status", "created_at", "user_id", "voucher_id") VALUES
(2,	'unclaimed',	'2022-06-12 18:31:46.446407+07',	1000,	NULL),
(1,	'unclaimed',	'2022-06-12 18:31:46.446407+07',	1000,	NULL),
(3,	'unclaimed',	'2022-06-12 18:31:46.446407+07',	1000,	NULL);

DROP TABLE IF EXISTS "user_vouchers";
DROP SEQUENCE IF EXISTS user_vouchers_id_seq;
CREATE SEQUENCE user_vouchers_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."user_vouchers" (
    "id" integer DEFAULT nextval('user_vouchers_id_seq') NOT NULL,
    "expired_at" timestamptz,
    "created_at" timestamptz NOT NULL,
    "voucher_id" integer,
    "user_id" integer,
    "voucher_status" character varying(32),
    CONSTRAINT "user_vouchers_pkey" PRIMARY KEY ("id"),
    CONSTRAINT "user_vouchers_voucher_id_fc77f02f_fk_vouchers_id" FOREIGN KEY (voucher_id) REFERENCES vouchers(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE
) WITH (oids = false);

CREATE INDEX "user_vouchers_voucher_id_fc77f02f" ON "public"."user_vouchers" USING btree ("voucher_id");

INSERT INTO "user_vouchers" ("id", "expired_at", "created_at", "voucher_id", "user_id", "voucher_status") VALUES
(1,	NULL,	'2022-06-12 17:39:42.175502+07',	1,	1000,	'Active'),
(2,	NULL,	'2022-06-12 17:39:49.990427+07',	2,	1000,	'Used'),
(3,	NULL,	'2022-06-12 17:39:49.990427+07',	3,	1000,	'Used');

DROP TABLE IF EXISTS "vouchers";
DROP SEQUENCE IF EXISTS vouchers_id_seq;
CREATE SEQUENCE vouchers_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1;

CREATE TABLE "public"."vouchers" (
    "id" integer DEFAULT nextval('vouchers_id_seq') NOT NULL,
    "reward_type" character varying(150),
    "terms" text,
    "title" text,
    "amount" integer,
    "discount_type" character varying(32),
    "is_active" boolean NOT NULL,
    "created_at" timestamptz NOT NULL,
    "thumbnail_active" text,
    "thumbnail_inactive" text,
    CONSTRAINT "vouchers_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "vouchers" ("id", "reward_type", "terms", "title", "amount", "discount_type", "is_active", "created_at", "thumbnail_active", "thumbnail_inactive") VALUES
(1,	'GrabCar',	'Lorem ipsum dolor sit amet',	'30% GrabCar Discount',	30,	'percentage',	'1',	'2022-06-12 17:33:34.660181+07',	'image',	'image'),
(2,	'GrabBike',	'Lorem ipsum dolor sit amet',	'GrabBike Discount 10.000',	10000,	'fixed',	'1',	'2022-06-12 17:36:11.165472+07',	'image',	'image_inactive'),
(3,	'GrabFood',	'Lorem ipsum dolor sit amet',	'GrabFood Discount 30.000',	10000,	'fixed',	'1',	'2022-06-12 17:36:11.165472+07',	'image',	'image_inactive');

-- 2022-06-19 15:08:40.786088+07
