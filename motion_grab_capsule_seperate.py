  def motion_grab_capsule_A(self):
        
        order_msg_A = 'A'
        order_msg_A_1 = 'aa'
        msg_A = 'a'
        
        code = self._arm.set_cgpio_analog(0, 5)
        print('motion_grab_capsule : set_cgpio_analog : 0,5 ')
        if not self._check_code(code, 'set_cgpio_analog'):
            return
        
        code = self._arm.set_cgpio_analog(1, 5)
        print('motion_grab_capsule : set_cgpio_analog : 1,5 ')
        if not self._check_code(code, 'set_cgpio_analog'):
            return

        # Joint Motion
        self._angle_speed = 100
        self._angle_acc = 100

        self._tcp_speed = 100
        self._tcp_acc = 1000

        code = self._arm.stop_lite6_gripper()
        print('motion_grab_capsule : _arm.stop_lite6_gripper 1 => ok ')
        if not self._check_code(code, 'stop_lite6_gripper'):
            return
        time.sleep(0.5)

        
        if order_msg_A_1 == 'aa':
            pass
            print('A WHAT???')
        else:
            code = self._arm.set_servo_angle(angle=[176, 31.7, 31, 76.7, 91.2, -1.9], speed=self._angle_speed,
                                                mvacc=self._angle_acc, wait=True, radius=0.0)
            print('Hmm.............. A?..')
            if not self._check_code(code, 'set_servo_angle'):
                return


        code = self._arm.open_lite6_gripper()
        print('_arm.stop_lite6_gripper 2 : ok ')
        if not self._check_code(code, 'open_lite6_gripper'):
            return
        time.sleep(1)


        if order_msg_A == 'A':
            code = self._arm.set_servo_angle(angle=[179.5, 33.5, 32.7, 113.0, 93.1, -2.3], speed=self._angle_speed,
                                                mvacc=self._angle_acc, wait=False, radius=20.0)
            print("move to A!!!!!!!!!!!!!!!!")
            if not self._check_code(code, 'set_servo_angle'):
                return

            code = self._arm.set_position(*self.position_jig_A_grab, speed=self._tcp_speed,
                                            mvacc=self._tcp_acc, radius=0.0, wait=True)
            print("move to A JIG !!!!!!!!!!!!!!!!")
            if not self._check_code(code, 'set_position'):
                return


        self._angle_speed = 180
        self._angle_acc = 500

        if msg_A == 'a':
            code = self._arm.set_servo_angle(angle=[145, -18.6, 10.5, 97.5, 81.4, 145], speed=self._angle_speed,
                                                mvacc=self._angle_acc, wait=False, radius=30.0)
            print("yes")
            if not self._check_code(code, 'set_servo_angle'):
                return
        else :
            code = self._arm.set_servo_angle(angle=[146.1, -10.7, 10.9, 102.7, 92.4, 24.9], speed=self._angle_speed,
                                            mvacc=self._angle_acc, wait=True, radius=0.0)
            print("no")
            if not self._check_code(code, 'set_servo_angle'):
                return





  def motion_grab_capsule_B(self):
      
        order_msg_B = 'B'
        msg_B = 'b'
      
        code = self._arm.set_cgpio_analog(0, 5)
        print('motion_grab_capsule : set_cgpio_analog : 0,5 ')
        if not self._check_code(code, 'set_cgpio_analog'):
            return
        
        code = self._arm.set_cgpio_analog(1, 5)
        print('motion_grab_capsule : set_cgpio_analog : 1,5 ')
        if not self._check_code(code, 'set_cgpio_analog'):
            return

        # Joint Motion
        self._angle_speed = 100
        self._angle_acc = 100

        self._tcp_speed = 100
        self._tcp_acc = 1000

        code = self._arm.stop_lite6_gripper()
        print('motion_grab_capsule : _arm.stop_lite6_gripper 1 => ok ')
        if not self._check_code(code, 'stop_lite6_gripper'):
            return
        time.sleep(0.5)


        if order_msg_B == 'B':

            code = self._arm.set_position(*self.position_jig_B_grab, speed=self._tcp_speed,
                                            mvacc=self._tcp_acc, radius=0.0, wait=True)
            print("move to B JIG !!!!!!!!!!!!!!!!")
            if not self._check_code(code, 'set_position'):
                return

        code = self._arm.close_lite6_gripper()
        print('_arm.stop_lite6_gripper 3 : ok ')
        if not self._check_code(code, 'close_lite6_gripper'):
            return

        time.sleep(1)

        self._angle_speed = 180
        self._angle_acc = 500

        if msg_B == 'b':
            code = self._arm.set_servo_angle(angle=[145, -18.6, 10.5, 97.5, 81.4, 145], speed=self._angle_speed,
                                                mvacc=self._angle_acc, wait=False, radius=30.0)
            print("yes")
            if not self._check_code(code, 'set_servo_angle'):
                return
        else :
            code = self._arm.set_servo_angle(angle=[146.1, -10.7, 10.9, 102.7, 92.4, 24.9], speed=self._angle_speed,
                                            mvacc=self._angle_acc, wait=True, radius=0.0)
            print("no")
            if not self._check_code(code, 'set_servo_angle'):
                return



  def motion_grab_capsule_C(self):
      
        order_msg_C = 'C'
        msg_C = 'c'
        msg_C_1 = 'cc'
      
        code = self._arm.set_cgpio_analog(0, 5)
        print('motion_grab_capsule : set_cgpio_analog : 0,5 ')
        if not self._check_code(code, 'set_cgpio_analog'):
            return
        
        code = self._arm.set_cgpio_analog(1, 5)
        print('motion_grab_capsule : set_cgpio_analog : 1,5 ')
        if not self._check_code(code, 'set_cgpio_analog'):
            return

        # Joint Motion
        self._angle_speed = 100
        self._angle_acc = 100

        self._tcp_speed = 100
        self._tcp_acc = 1000

        code = self._arm.stop_lite6_gripper()
        print('motion_grab_capsule : _arm.stop_lite6_gripper 1 => ok ')
        if not self._check_code(code, 'stop_lite6_gripper'):
            return
        time.sleep(0.5)

      
        if order_msg_C == 'C':
            code = self._arm.set_servo_angle(angle=[182.6, 27.8, 27.7, 55.7, 90.4, -6.4], speed=self._angle_speed,
                                                mvacc=self._angle_acc, wait=False, radius=20.0)
            print("move to C !!!!!!!!!!!!!!!!")
            if not self._check_code(code, 'set_servo_angle'):
                return

            code = self._arm.set_position(*self.position_jig_C_grab, speed=self._tcp_speed,
                                            mvacc=self._tcp_acc, radius=0.0, wait=True)
            print("move to C JIG !!!!!!!!!!!!!!!!")
            if not self._check_code(code, 'set_position'):
                return

        code = self._arm.close_lite6_gripper()
        print('_arm.stop_lite6_gripper 3 : ok ')
        if not self._check_code(code, 'close_lite6_gripper'):
            return

        time.sleep(1)
        
        if msg_C == 'C':
            code = self._arm.set_position(z=150, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                            wait=False)
            print("move to C 2 !!!!!!!!!!!!!!!!")
            if not self._check_code(code, 'set_position'):
                return
            self._tcp_speed = 200
            self._tcp_acc = 1000
            code = self._arm.set_tool_position(*[0.0, 0.0, -90.0, 0.0, 0.0, 0.0], speed=self._tcp_speed,
                                                mvacc=self._tcp_acc, wait=False)
            print("TOOL !!!!!!!!!!!!!!!!")
            if not self._check_code(code, 'set_position'):
                return
        else:
            code = self._arm.set_position(z=100, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                            wait=False)
            print("TOOL2 !!!!!!!!!!!!!!!!")
            if not self._check_code(code, 'set_position'):
                return


        self._angle_speed = 180
        self._angle_acc = 500

        if msg_C_1 == ['cc']:
            code = self._arm.set_servo_angle(angle=[145, -18.6, 10.5, 97.5, 81.4, 145], speed=self._angle_speed,
                                                mvacc=self._angle_acc, wait=False, radius=30.0)
            print("yes")
            if not self._check_code(code, 'set_servo_angle'):
                return
        else:
            code = self._arm.set_servo_angle(angle=[146.1, -10.7, 10.9, 102.7, 92.4, 24.9], speed=self._angle_speed,
                                            mvacc=self._angle_acc, wait=True, radius=0.0)
            print("no")
            if not self._check_code(code, 'set_servo_angle'):
                return
            
            