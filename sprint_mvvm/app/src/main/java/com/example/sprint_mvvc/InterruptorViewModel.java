package com.example.sprint_mvvc;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class InterruptorViewModel extends ViewModel {
    // Estado: ¿Está encendido?
    private final MutableLiveData<Boolean> _encendido = new MutableLiveData<>(false);

    public LiveData<Boolean> getEstado() { return _encendido; }

    public void alternar() {
        // Leemos el valor actual y lo invertimos
        boolean valorActual = Boolean.TRUE.equals(_encendido.getValue());
        _encendido.setValue(!valorActual);
    }
}