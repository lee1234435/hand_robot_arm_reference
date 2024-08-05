_   def motion_make_icecream_a(self):
        time.sleep(5)

        code = self._arm.set_position(z=-20, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                        wait=True)
        if not self._check_code(code, 'set_position'):
            return

        time.sleep(2)

        
        code = self._arm.set_cgpio_digital(3, 0, delay_sec=0)
        if not self._check_code(code, 'set_cgpio_digital'):
            return
        
        time.sleep(0.5)


    def motion_make_icecream_b(self):
        time.sleep(5)
        
        code = self._arm.set_position(z=-10, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                        wait=True)
    
        if not self._check_code(code, 'set_position'):
            return
        
        time.sleep(2)
        
        code = self._arm.set_cgpio_digital(3, 0, delay_sec=0)
        if not self._check_code(code, 'set_cgpio_digital'):
            return
        
        time.sleep(0.5)
    
    def motion_make_icecream_c(self): 
        time.sleep(5) 
                
        code = self._arm.set_position(z=-50, radius=0, speed=self._tcp_speed, mvacc=self._tcp_acc, relative=True,
                                        wait=True)
        if not self._check_code(code, 'set_position'):
            return
        
        time.sleep(1)
        
        code = self._arm.set_cgpio_digital(3, 0, delay_sec=0)
        if not self._check_code(code, 'set_cgpio_digital'):
            return
        
        time.sleep(0.5)