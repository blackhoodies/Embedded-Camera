package com.example.android.hethongnhung.Controller;

import android.content.Context;
import android.content.SharedPreferences;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

public class StoreData {
    private static final String fileName = "IPsetting";

    public static JSONObject loadData(Context context) throws JSONException {
        SharedPreferences sharedPreferences = context.getSharedPreferences(fileName, Context.MODE_PRIVATE);
        JSONObject returner = new JSONObject();

        if (sharedPreferences != null){
            returner.put("address", sharedPreferences.getString("address", "www.youtube.com"));
            returner.put("port", sharedPreferences.getInt("port", 80));
        } else{
            Toast.makeText(context, "Cần cài đặt thông tin ban đầu", Toast.LENGTH_SHORT).show();
            return null;
        }

        return returner;
    }

    public static void saveData(Context context, String address, int port){
        SharedPreferences sharedPreferences = context.getSharedPreferences(fileName, Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sharedPreferences.edit();

        editor.putString("address", address);
        editor.putInt("port", port);

        editor.apply();

        Toast.makeText(context, "Lưu thành công", Toast.LENGTH_SHORT).show();
    }
}
