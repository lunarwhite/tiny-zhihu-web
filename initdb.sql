USE [master]
GO
/****** Object:  Database [izhihu]    Script Date: 2021/6/19 13:14:24 ******/
CREATE DATABASE [izhihu]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'izhihu', FILENAME = N'/var/opt/mssql/data/izhihu.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'izhihu_log', FILENAME = N'/var/opt/mssql/data/izhihu_Log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [izhihu] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [izhihu].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [izhihu] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [izhihu] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [izhihu] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [izhihu] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [izhihu] SET ARITHABORT OFF 
GO
ALTER DATABASE [izhihu] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [izhihu] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [izhihu] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [izhihu] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [izhihu] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [izhihu] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [izhihu] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [izhihu] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [izhihu] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [izhihu] SET  DISABLE_BROKER 
GO
ALTER DATABASE [izhihu] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [izhihu] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [izhihu] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [izhihu] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [izhihu] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [izhihu] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [izhihu] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [izhihu] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [izhihu] SET  MULTI_USER 
GO
ALTER DATABASE [izhihu] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [izhihu] SET DB_CHAINING OFF 
GO
ALTER DATABASE [izhihu] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [izhihu] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [izhihu] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [izhihu] SET QUERY_STORE = OFF
GO
USE [izhihu]
GO
/****** Object:  Table [dbo].[Account_info]    Script Date: 2021/6/19 13:14:26 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Account_info](
	[passwd] [varchar](20) NOT NULL,
	[Mobile] [bigint] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Mobile] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[user_account]    Script Date: 2021/6/19 13:14:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[user_account](mobile,passwd)
as
select Mobile,passwd
from Account_info
with check option;

--建立索引
GO
/****** Object:  Table [dbo].[Answer_info]    Script Date: 2021/6/19 13:14:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Answer_info](
	[A_ID] [int] IDENTITY(1,1) NOT NULL,
	[Q_ID] [int] NOT NULL,
	[U_id] [int] NOT NULL,
	[A_text] [text] NOT NULL,
	[C_Number] [bigint] NULL,
	[Z_Number] [bigint] NULL,
PRIMARY KEY CLUSTERED 
(
	[A_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Collection_info]    Script Date: 2021/6/19 13:14:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Collection_info](
	[Q_ID] [int] NOT NULL,
	[u_ID] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Q_ID] ASC,
	[u_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Comment_info]    Script Date: 2021/6/19 13:14:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Comment_info](
	[C_ID] [int] IDENTITY(1,1) NOT NULL,
	[A_ID] [int] NOT NULL,
	[U_id] [int] NOT NULL,
	[C_text] [text] NOT NULL,
	[postTime] [datetime] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[C_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Focus_info]    Script Date: 2021/6/19 13:14:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Focus_info](
	[A_user_ID] [int] NOT NULL,
	[B_user_ID] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[A_user_ID] ASC,
	[B_user_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Question_info]    Script Date: 2021/6/19 13:14:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Question_info](
	[Q_ID] [int] IDENTITY(1,1) NOT NULL,
	[U_id] [int] NOT NULL,
	[Q_title] [text] NOT NULL,
	[Q_text] [text] NOT NULL,
	[postTime] [datetime] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[Q_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[User_info]    Script Date: 2021/6/19 13:14:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[User_info](
	[U_id] [int] IDENTITY(1,1) NOT NULL,
	[UserName] [varchar](20) NOT NULL,
	[Mobile] [bigint] NOT NULL,
	[Email] [varchar](20) NOT NULL,
	[Sex] [varchar](20) NULL,
	[RegTime] [datetime] NULL,
	[SignDetail] [text] NULL,
PRIMARY KEY CLUSTERED 
(
	[U_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [c_1] UNIQUE NONCLUSTERED 
(
	[Mobile] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Index [idx_2]    Script Date: 2021/6/19 13:14:27 ******/
CREATE NONCLUSTERED INDEX [idx_2] ON [dbo].[Answer_info]
(
	[Q_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [idx_l]    Script Date: 2021/6/19 13:14:27 ******/
CREATE NONCLUSTERED INDEX [idx_l] ON [dbo].[Comment_info]
(
	[A_ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Account_info] ADD  CONSTRAINT [ab_e]  DEFAULT ('pwd') FOR [passwd]
GO
ALTER TABLE [dbo].[Answer_info] ADD  DEFAULT (' 0') FOR [C_Number]
GO
ALTER TABLE [dbo].[Answer_info] ADD  DEFAULT (' 0') FOR [Z_Number]
GO
ALTER TABLE [dbo].[Question_info] ADD  CONSTRAINT [ab_d]  DEFAULT (getdate()) FOR [postTime]
GO
ALTER TABLE [dbo].[User_info] ADD  DEFAULT ('男') FOR [Sex]
GO
ALTER TABLE [dbo].[User_info] ADD  CONSTRAINT [ab_c]  DEFAULT (getdate()) FOR [RegTime]
GO
ALTER TABLE [dbo].[Answer_info]  WITH CHECK ADD  CONSTRAINT [Q_fk] FOREIGN KEY([Q_ID])
REFERENCES [dbo].[Question_info] ([Q_ID])
GO
ALTER TABLE [dbo].[Answer_info] CHECK CONSTRAINT [Q_fk]
GO
ALTER TABLE [dbo].[Answer_info]  WITH CHECK ADD  CONSTRAINT [user_fk_2] FOREIGN KEY([U_id])
REFERENCES [dbo].[User_info] ([U_id])
GO
ALTER TABLE [dbo].[Answer_info] CHECK CONSTRAINT [user_fk_2]
GO
ALTER TABLE [dbo].[Collection_info]  WITH CHECK ADD  CONSTRAINT [Q_fk_1] FOREIGN KEY([Q_ID])
REFERENCES [dbo].[Question_info] ([Q_ID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[Collection_info] CHECK CONSTRAINT [Q_fk_1]
GO
ALTER TABLE [dbo].[Collection_info]  WITH CHECK ADD  CONSTRAINT [user_fk_4] FOREIGN KEY([u_ID])
REFERENCES [dbo].[User_info] ([U_id])
GO
ALTER TABLE [dbo].[Collection_info] CHECK CONSTRAINT [user_fk_4]
GO
ALTER TABLE [dbo].[Comment_info]  WITH CHECK ADD  CONSTRAINT [A_fk] FOREIGN KEY([A_ID])
REFERENCES [dbo].[Answer_info] ([A_ID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[Comment_info] CHECK CONSTRAINT [A_fk]
GO
ALTER TABLE [dbo].[Comment_info]  WITH CHECK ADD  CONSTRAINT [user_fk_3] FOREIGN KEY([U_id])
REFERENCES [dbo].[User_info] ([U_id])
GO
ALTER TABLE [dbo].[Comment_info] CHECK CONSTRAINT [user_fk_3]
GO
ALTER TABLE [dbo].[Focus_info]  WITH CHECK ADD  CONSTRAINT [user_fk_5] FOREIGN KEY([A_user_ID])
REFERENCES [dbo].[User_info] ([U_id])
GO
ALTER TABLE [dbo].[Focus_info] CHECK CONSTRAINT [user_fk_5]
GO
ALTER TABLE [dbo].[Focus_info]  WITH CHECK ADD  CONSTRAINT [user_fk_6] FOREIGN KEY([B_user_ID])
REFERENCES [dbo].[User_info] ([U_id])
GO
ALTER TABLE [dbo].[Focus_info] CHECK CONSTRAINT [user_fk_6]
GO
ALTER TABLE [dbo].[Question_info]  WITH CHECK ADD  CONSTRAINT [user_fk_1] FOREIGN KEY([U_id])
REFERENCES [dbo].[User_info] ([U_id])
GO
ALTER TABLE [dbo].[Question_info] CHECK CONSTRAINT [user_fk_1]
GO
ALTER TABLE [dbo].[User_info]  WITH CHECK ADD CHECK  (([Mobile]>=(10000000000.) AND [Mobile]<=(99999999999.)))
GO
/****** Object:  StoredProcedure [dbo].[Question_Answer]    Script Date: 2021/6/19 13:14:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[Question_Answer] @Q_ID int
AS
select A_id,Q_title,Q_text
from Question_info as Q ,Answer_info as A
where Q.Q_ID = @Q_ID and @Q_ID =A.Q_ID
GO
USE [master]
GO
ALTER DATABASE [izhihu] SET  READ_WRITE 
GO