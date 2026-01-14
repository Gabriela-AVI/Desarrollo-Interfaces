package com.example.sprint_mvvc;

import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;


public class MainActivity extends AppCompatActivity {

    // En el onCreate...
    InterruptorViewModel vm = new ViewModelProvider(this).get(InterruptorViewModel.class);
    View fondo = findViewById(R.id.layoutFondo);
    Button boton = findViewById(R.id.btnInterruptor);

// 1. OBSERVAR: Si el dato cambia, pintamos el fondo
    vm.getEstado().observe(this, esEncendido -> {
        if (esEncendido) {
            fondo.setBackgroundColor(Color.YELLOW);
            boton.setText("APAGAR");
        } else {
            fondo.setBackgroundColor(Color.GRAY);
            boton.setText("ENCENDER");
        }
    });

// 2. EVENTO: Al hacer clic, solo avisamos al VM
boton.setOnClickListener(v -> vm.alternar());
}