package com.example.kyc.controller;

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
