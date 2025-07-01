from flask import request
from datetime import datetime
from flask import send_file,request
# from werkzeug.utils import send_file

from model.user_model import user_model
obj=user_model()
def register_route(app):
    @app.route("/user/getall",methods=["GET"])
    def user_getall_controller():
        return obj.user_getall_model()


    @app.route("/user/addone",methods=["POST"])
    def user_addone_controller():
        return obj.user_addone_model(request.form)

    @app.route("/user/update", methods=["PUT"])
    def user_update_controller():
        return obj.user_update_model(request.form)

    @app.route("/user/delete/<id>", methods=["DELETE"])
    def user_delete_controller(id):
        return obj.user_delete_model(id)

    @app.route("/user/patch/<id>",methods=["PATCH"])
    def user_patch_controller(id):
        return obj.user_patch_model(request.args,id)

    @app.route("/user/getall/limit/<limit>/page/<page>",methods=["GET"])
    def user_pagination_controller(limit,page):
        return obj.user_pagination_model(limit,page)


    @app.route("/user/<uid>/upload/avatar" ,methods=["PUT"])
    def user_upload_controller(uid):
        file=request.files['avatar']
        unique=str(datetime.now().timestamp()).replace(".","")
        final_path = f"Uploads/{unique}{file.filename}"
        file.save(final_path)


        return  obj.user_upload_model(uid,final_path)

    @app.route("/uploads/<filename>")
    def user_getavatar_controller(filename):
        return send_file(f"uploads/{filename}")




