package com.example.android.hethongnhung.Controller;

import android.util.Log;

public class Utils {
    public static boolean checkIPAddress(String ipAddress){
        if (ipAddress.isEmpty()){
            return false;
        }
        String regex = "^([\\d]{1,3}[.]){3}[\\d]{1,3}$";
        return ipAddress.matches(regex);
    }

    public static boolean checkPortNumber(String portNumber){
        if (portNumber.isEmpty()){
            return false;
        }
        String regex = "^\\d{1,5}$";
        if (portNumber.matches(regex)){
            long tmp = 0;
            try{
                tmp = Long.parseLong(portNumber);
                if (tmp <= 65535L){
                    return true;
                }
            } catch (Exception e){
                Log.e("UtilsCheckPortNumber", "Loi chuyen doi String -> Long");
            }
        }
        return false;
    }
}
