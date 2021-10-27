<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@page import="java.sql.PreparedStatement"%>

<%@page language="java" contentType="text/html; charset=UTF-8"%>
<%!Connection conn = null;
	PreparedStatement pstmt = null;
	String url = "jdbc:oracle:thin:@localhost:1521:XE";
	String uid = "hr";
	String pass = "1234";
	String sql = "insert into member values(?,?,?,?,?,?)";%>


<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%
	request.setCharacterEncoding("UTF-8");
	String name = request.getParameter("name");
	String userid = request.getParameter("userid");
	String userpwd = request.getParameter("userpwd");
	String email = request.getParameter("email");
	String phone = request.getParameter("phone");
	String admin = request.getParameter("admin");
	try {
		//(1단계) JDBC 드라이버 루트
		Class.forName("oracle.jdbc.driver.OracleDriver");
		//(2단계) 데이터베이스 연결 객체인 Connection생성
		conn = DriverManager.getConnection(url, uid, pass);
		//(3단계)statement 객체 생성하기
		pstmt = conn.prepareStatement(sql);
		//(4단계) 바인딩 변수를 채운다.
		pstmt.setString(1, name);
		pstmt.setString(2, userid);
		pstmt.setString(3, userpwd);
		pstmt.setString(4, email);
		pstmt.setString(5, phone);
		pstmt.setInt(6, Integer.parseInt(admin));
		//(5단계)SQL문을 실행하여 결과처리
		pstmt.executeUpdate();
	} catch (Exception e) {
		e.printStackTrace();
	} finally {
		//(6단계)사용한 리소스 해제
		try {
			if (pstmt != null)
		pstmt.close();
			if (conn != null)
		conn.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	} //finally의 끝
	%>
	<h3>회원가입성공</h3>
	<a href="01_allMember.jsp"> 회원 전체 목록 보기</a>
</body>
</html>