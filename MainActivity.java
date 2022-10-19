package com.example.trailmakingtest;

import androidx.appcompat.app.AppCompatActivity;

import android.content.*;
import android.os.Bundle;
import android.view.View;
import android.widget.*;

public class MainActivity extends AppCompatActivity {

    private Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        button = (Button) findViewById(R.id.btnNextPage);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openTMT();
            }
        });

    }

    public void openTMT() {
        Intent intent = new Intent(this, tmt.class);
        startActivity(intent);
    }


    public void onBtnClick (View view) {
        TextView txtFirstName = findViewById(R.id.txtFirstName);
        TextView txtLastName = findViewById(R.id.txtLastName);
        TextView txtEmail = findViewById(R.id.txtEmail);

        EditText edtTxtFirstName = findViewById(R.id.edtTxtFirstName);
        EditText edtTxtLastName = findViewById(R.id.edtTxtLastName);
        EditText edtTxtEmail = findViewById(R.id.edtTxtEmail);

        txtFirstName.setText("First Name: " + edtTxtFirstName.getText().toString());
        txtLastName.setText("Last Name: " + edtTxtLastName.getText().toString());
        txtEmail.setText("Email: " + edtTxtEmail.getText().toString());

    }
}