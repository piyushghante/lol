package com.example.kyc.service;

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
