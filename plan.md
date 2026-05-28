# ROS2 4-Week Learning & Portfolio Project Plan

This plan is designed to take you from basic ROS2 knowledge (nodes, topics, messages) to a **job-ready robotics portfolio project** using ROS 2.

The final goal is to build:

> 🤖 An autonomous mobile robot in simulation with SLAM + navigation + optional perception

---

# 🧭 Week 1 — ROS2 Fundamentals + Robot Description

## 🎯 Goal

Understand ROS2 core concepts deeply and build your first robot model.

---

## 📚 Concepts to Learn

### ROS2 Core

* Nodes
* Topics
* Services
* Actions
* Parameters
* Packages and workspaces (colcon)
* Launch files

### Communication Model

* Publisher / Subscriber pattern
* Message types
* QoS basics (reliability, durability)

### TF2 (VERY IMPORTANT)

* coordinate frames
* static vs dynamic transforms
* robot frame hierarchy

---

## 🛠️ Practical Tasks

### 1. Setup workspace

* Create `ros2_ws`
* Build with `colcon build`
* Source environment properly

### 2. Create basic nodes

* Publisher node (robot status / heartbeat)
* Subscriber node (control or logging)

### 3. Build robot description

* URDF/Xacro robot model
* Differential drive robot:

  * base_link
  * wheels
  * lidar frame

### 4. Visualize in RViz

* Load robot model
* Display TF tree

---

## ✅ Deliverables

* ROS2 workspace working
* Simple pub/sub system
* Robot URDF visualized in RViz
* TF tree correctly displayed

---

## ⚠️ Common pitfalls

* Forgetting to source ROS2 setup
* Broken TF tree (wrong frame names)
* URDF errors (missing links/joints)

---

# 🧭 Week 2 — Simulation + Sensors + Control

## 🎯 Goal

Run a simulated robot in a physics environment and control it.

---

## 📚 Concepts to Learn

### Gazebo Integration

* Robot spawning
* Plugins
* Physics simulation basics

### Robot Control

* cmd_vel interface
* differential drive kinematics

### Sensors

* LiDAR simulation
* IMU basics
* sensor noise concept

---

## 🛠️ Practical Tasks

### 1. Gazebo setup

* Create empty world
* Add obstacles

### 2. Spawn robot

* Load URDF into Gazebo
* Verify physics interaction

### 3. Add sensors

* LiDAR sensor
* publish `/scan` topic

### 4. Control robot

* Teleop keyboard
* Manual motion using `/cmd_vel`

---

## 🧪 Integration check

* Robot moves in Gazebo
* RViz shows:

  * robot model
  * LiDAR scan

---

## ✅ Deliverables

* Working Gazebo simulation
* Controllable robot
* Sensor data streaming into ROS2

---

## ⚠️ Common pitfalls

* Incorrect plugin setup
* TF mismatch between Gazebo and RViz
* Missing sensor frames

---

# 🧭 Week 3 — SLAM + Autonomous Navigation (Core Value Week)

## 🎯 Goal

Make the robot map the environment and navigate autonomously.

---

## 📚 Concepts to Learn

### SLAM

* Occupancy grid maps
* Pose estimation
* SLAM pipeline

### Navigation Stack

* Global planner
* Local planner
* Costmaps
* Recovery behaviors

### Behavior Trees (important modern concept)

---

## 🛠️ Practical Tasks

### 1. SLAM setup

* Install and configure SLAM Toolbox
* Generate map from exploration

### 2. Map building

* Drive robot manually
* Generate static map

### 3. Navigation (Nav2)

* Configure Nav2 stack
* Set goal in RViz
* Robot navigates autonomously

---

## 🧪 Integration check

Robot should:

* build map
* localize itself
* navigate to target points

---

## ✅ Deliverables

* SLAM working system
* Navigation working system
* RViz showing map + robot pose

---

## ⚠️ Common pitfalls

* Incorrect TF tree (map → odom → base_link)
* Costmap configuration issues
* Poor localization due to bad LiDAR setup

---

# 🧭 Week 4 — Portfolio Upgrade + Intelligence Layer

## 🎯 Goal

Transform project into a professional portfolio-grade system.

---

## 📚 Concepts to Add

Choose ONE enhancement path:

---

## 🧠 Option A — Perception (Computer Vision)

* Camera integration
* Object detection (YOLO/OpenCV)
* Publishing detection topics

---

## 📡 Option B — Sensor Fusion (Highly Recommended)

* EKF / UKF filtering
* robot_localization package
* fuse:

  * odometry
  * IMU
  * LiDAR

---

## 🧠 Option C — Behavior Logic Upgrade

* Behavior Trees customization
* Mission-based logic:

  * explore → detect → navigate → return

---

## 🛠️ Engineering Polish (VERY IMPORTANT)

### 1. Dockerization

* Full ROS2 environment in Docker
* One-command startup

### 2. Launch system cleanup

* modular launch files
* parameterized configs

### 3. Documentation

* architecture diagram
* setup instructions
* system explanation

### 4. Demo content

* GIF or video of robot
* screenshots from RViz/Gazebo

---

## ✅ Final Deliverables

* Fully working autonomous robot system
* Clean GitHub repository
* Dockerized project
* Demo video/GIF
* Documentation ready for recruiters

---

# 🏆 Final Outcome

By completing this plan, you will have:

* Strong ROS2 fundamentals
* Practical simulation experience
* SLAM + Nav2 mastery
* A portfolio-grade robotics project
* Skills aligned with real robotics job requirements

---

# 🚀 Success Criteria

You are job-ready when you can confidently explain:

* TF tree structure (map → odom → base_link)
* Nav2 architecture
* SLAM pipeline
* How sensors integrate into ROS2
* How nodes communicate in a distributed system

---

