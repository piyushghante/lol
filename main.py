import os

# Define the directory structure
dirs = [
    "src/main/java/com/example/kyc",
    "src/main/java/com/example/kyc/controller",
    "src/main/java/com/example/kyc/model",
    "src/main/java/com/example/kyc/repository",
    "src/main/java/com/example/kyc/service",
    "src/main/resources",
    "src/main/resources/templates"
]

# Define the file content
files = {
    "pom.xml": """<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>kyc</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <packaging>jar</packaging>
    <name>kyc</name>
    <description>Dummy KYC Application</description>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.4</version>
        <relativePath/>
    </parent>

    <dependencies>
        <!-- Spring Boot Starter Web -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <!-- Spring Boot Starter Data JPA -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>

        <!-- H2 Database -->
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>runtime</scope>
        </dependency>

        <!-- Thymeleaf -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-thymeleaf</artifactId>
        </dependency>

        <!-- Spring Boot Starter Test -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>
""",
    "src/main/java/com/example/kyc/KycApplication.java": """package com.example.kyc;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class KycApplication {
    public static void main(String[] args) {
        SpringApplication.run(KycApplication.class, args);
    }
}
""",
    "src/main/java/com/example/kyc/model/Customer.java": """package com.example.kyc.model;

import javax.persistence.*;
import java.time.LocalDate;

@Entity
public class Customer {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private LocalDate dateOfBirth;
    private String panCard;
    private String address;
    private String city;
    private Double accountBalance;

    // Getters and Setters

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public LocalDate getDateOfBirth() {
        return dateOfBirth;
    }

    public void setDateOfBirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public String getPanCard() {
        return panCard;
    }

    public void setPanCard(String panCard) {
        this.panCard = panCard;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public Double getAccountBalance() {
        return accountBalance;
    }

    public void setAccountBalance(Double accountBalance) {
        this.accountBalance = accountBalance;
    }
}
""",
    "src/main/java/com/example/kyc/repository/CustomerRepository.java": """package com.example.kyc.repository;

import com.example.kyc.model.Customer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CustomerRepository extends JpaRepository<Customer, Long> {
    List<Customer> findByCityOrderByAccountBalanceDesc(String city);
}
""",
    "src/main/java/com/example/kyc/service/CustomerService.java": """package com.example.kyc.service;

import com.example.kyc.model.Customer;
import com.example.kyc.repository.CustomerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CustomerService {

    @Autowired
    private CustomerRepository customerRepository;

    public List<Customer> findCustomersByCity(String city) {
        return customerRepository.findByCityOrderByAccountBalanceDesc(city);
    }
}
""",
    "src/main/java/com/example/kyc/controller/CustomerController.java": """package com.example.kyc.controller;

import com.example.kyc.model.Customer;
import com.example.kyc.service.CustomerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
public class CustomerController {

    @Autowired
    private CustomerService customerService;

    @GetMapping("/")
    public String home() {
        return "index";
    }

    @GetMapping("/search")
    public String search(@RequestParam("city") String city, Model model) {
        List<Customer> customers = customerService.findCustomersByCity(city);
        model.addAttribute("customers", customers);
        return "result";
    }
}
""",
    "src/main/resources/application.properties": """spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.h2.console.enabled=true
spring.h2.console.path=/h2-console
""",
    "src/main/resources/data.sql": """INSERT INTO customer (name, date_of_birth, pan_card, address, city, account_balance) VALUES
('John Doe', '1985-05-20', 'ABCDE1234F', '123 Main St', 'Pune', 5000.00),
('Jane Smith', '1990-08-15', 'XYZAB5678C', '456 Market St', 'Mumbai', 15000.00),
('Alice Johnson', '1982-12-01', 'LMNOP1234Q', '789 Broadway', 'Pune', 20000.00);
""",
    "src/main/resources/templates/index.html": """<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>KYC Search</title>
</head>
<body>
    <h1>Search Customer by City</h1>
    <form action="/search" method="get">
        <label for="city">City:</label>
        <input type="text" id="city" name="city">
        <button type="submit">Search</button>
    </form>
</body>
</html>
""",
    "src/main/resources/templates/result.html": """<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Search Results</title>
</head>
<body>
    <h1>Search Results</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Date of Birth</th>
                <th>PAN Card</th>
                <th>Address</th>
                <th>City</th>
                <th>Account Balance</th>
            </tr>
        </thead>
        <tbody>
            <tr th:each="customer : ${customers}">
                <td th:text="${customer.name}"></td>
                <td th:text="${customer.dateOfBirth}"></td>
                <td th:text="${customer.panCard}"></td>
                <td th:text="${customer.address}"></td>
                <td th:text="${customer.city}"></td>
                <td th:text="${customer.accountBalance}"></td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""
}

# Create directories
for dir in dirs:
    os.makedirs(dir, exist_ok=True)

# Create files with content
for file, content in files.items():
    with open(file, 'w') as f:
        f.write(content)

print("Project structure created successfully!")
