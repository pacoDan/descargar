.PHONY: install uninstall create_dir move_executable remove_executable



# Regla principal: instalación completa
install: create_dir
	@echo "Creando el entorno virtual..."
	python -m venv env
	@echo "Activando el entorno virtual y instalando dependencias..."
	$(SHELL) -c "source env/bin/activate && pip install -r requirements.txt"
	@echo "Generando el ejecutable..."
	$(SHELL) -c "source env/bin/activate && pyinstaller --onefile descargar.py"
	@$(MAKE) move_executable
	@$(MAKE) update_path

# Regla para desinstalar: eliminar el ejecutable de ~/.miBin
uninstall: remove_executable
	@echo "Desinstalación completada."

# Regla para crear la carpeta ~/.miBin si no existe
create_dir:
	@if [ ! -d "$$HOME/.miBin" ]; then \
		echo "Creando la carpeta ~/.miBin..."; \
		mkdir "$$HOME/.miBin"; \
	fi

# Regla para mover el ejecutable a ~/.miBin
move_executable:
	@echo "Moviendo el ejecutable a ~/.miBin..."
	mv ./dist/descargar ~/.miBin
	@echo "Ejecutable movido correctamente a ~/.miBin."
# Regla para actualizar el PATH y recargar la shell
update_path:
	@if ! echo "$$PATH" | grep -q "$$HOME/.miBin"; then \
		echo "Agregando ~/.miBin al PATH en .bashrc..."; \
		echo 'export PATH=$$HOME/.miBin:$$PATH' >> $$HOME/.bashrc; \
		source $$HOME/.bashrc; \
		echo "PATH actualizado correctamente."; \
	else \
		echo "~/.miBin ya está en el PATH."; \
	fi

# Regla para eliminar el ejecutable de ~/.miBin
remove_executable:
	rm "$$HOME/.miBin/descargar"

clean:
	rm -rf env
	rm -rf dist
	rm -rf build
	rm -rf __pycache__
	rm -rf *.spec
