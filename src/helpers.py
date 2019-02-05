from constants import Constants
from tween import TweenEaseType
from enums import *
import random

class LittleHelpers:
    @staticmethod
    def is_known_notation(str):
        for move in Constants.KNOWN_NOTATIONS:
            if move == str:
                return True
        return False

    @staticmethod
    def get_face_rotation_by_notation(str):
        return Constants.NOTATION_TO_FACE_ROTATION_MAP.get(str)

    @staticmethod
    def get_notation_by_face_rotation(face):
        return Constants.FACE_ROTATION_TO_NOTATION_MAP.get(face)

    @staticmethod
    def is_cw_face_rotation(face):
        for cw in Constants.CW_FACE_ROTATIONS:
            if face == cw:
                return True
        return False

    @staticmethod
    def is_ccw_face_rotation(face):
        for ccw in Constants.CCW_FACE_ROTATION:
            if face == ccw:
                return True
        return False

    @staticmethod
    # expand notations like "R2" to "R R"
    # not supported are notations like "R2'"
    def expand_notations(moves):
        expanded_notations = []
        for move in moves:
            if not LittleHelpers.is_known_notation(move):
                return []
            length = len(move)
            if length == 1:
                expanded_notations.append(move)
            elif length == 2:
                if move[1] == '2':
                    expanded_notations.append(move[0])
                    expanded_notations.append(move[0])
                elif move[1] == Constants.PRIME:
                    expanded_notations.append(move)
            elif length == 3:
                if move[1] == '2' and move[2] == Constants.PRIME:
                    m = move[0] + Constants.PRIME
                    expanded_notations.append(m)
                    expanded_notations.append(m)
            else:
                return []
        return expanded_notations

    @staticmethod
    def translate_moves_to_face_rotations(moves):
        face_rotations = []
        for move in moves:
            if not LittleHelpers.is_known_notation(move):
                return []
            face_rotation = LittleHelpers.get_face_rotation_by_notation(move)
            if face_rotation != None:
                face_rotations.append(face_rotation)
            else:
                return []
        return face_rotations

    @staticmethod
    def build_color_orienation_string(color_mapping):
        try:
            front = Constants.FACE_TO_NAME_MAP.get(Face.FRONT)
            back = Constants.FACE_TO_NAME_MAP[Face.BACK]
            left = Constants.FACE_TO_NAME_MAP[Face.LEFT]
            right = Constants.FACE_TO_NAME_MAP[Face.RIGHT]
            up = Constants.FACE_TO_NAME_MAP[Face.UP]
            down = Constants.FACE_TO_NAME_MAP[Face.DOWN]

            fname = color_mapping[front]
            bname = color_mapping[back]
            lname = color_mapping[left]
            rname = color_mapping[right]
            uname = color_mapping[up]
            dname = color_mapping[down]

            # format: "front:blue, back:green, right:red, left:orange, up:yellow, down:white"
            return '{0}:{1},{2}:{3},{4}:{5},{6}:{7},{8}:{9},{10}:{11}'.format(front, fname, back, bname, right, rname, left, lname, up, uname, down, dname)
        except:
            print('Big Nope.')
        return ''

    @staticmethod
    def get_mapped_color(face_type, color_mapping, colors):
        try:
            face_name = Constants.FACE_TO_NAME_MAP[face_type]
            color_name = color_mapping[face_name]
            color = colors[color_name]
            return color
        except:
            print('Big Nope.')
        return Constants.FALLBACK_COLOR

    @staticmethod
    def make_color_mapping_from_string(str):
        arr = str.upper().split(",")
        if len(arr) != 6:
            return {}
        color_mapping = {}
        try:
            for face_to_color in arr:
                face_and_color = face_to_color.split(":")
                if len(face_and_color) != 2:
                    return {}
                face = face_and_color[0].strip().lower()
                color = face_and_color[1].strip().lower()
                color_mapping[face] = color
        except:
            pass
        return color_mapping

    @staticmethod
    def get_patterns():
        return [
            Constants.CHECKERBOARD_PATTERN,
            Constants.CUBE_IN_CUBE_PATTERN,
            Constants.FOUR_CROSSES_PATTERN,
            Constants.FOUR_SPOTS_PATTERN,
            Constants.GIFT_BOX_PATTERN,
            Constants.HI_AGAIN_PATTERN,
            Constants.HI_ALL_AROUND_PATTERN,
            Constants.PLUS_MINUS_PATTERN,
            Constants.SIX_SPOTS_PATTERN,
            Constants.SPEEDSOLVER_PATTERN,
            Constants.SUPERFLIP_PATTERN,
            Constants.TETRIS_PATTERN,
            Constants.UNION_JACK_PATTERN,
            Constants.VERTICAL_STRIPES_PATTERN,
            Constants.WIRE_PATTERN
        ]

    @staticmethod
    def get_random_pattern():
        return random.choice(LittleHelpers.get_patterns())

    @staticmethod
    def convert_str_to_float(str, default=None):
        try:
            return float(str)
        except ValueError:
            print('Big Nope. Given value cannot be converted to a float.')
        return default

    @staticmethod
    def get_ease_type_by_str(str):
        if str == 'ease_linear': return TweenEaseType.EASE_LINEAR
        if str == 'ease_in_sine': return TweenEaseType.EASE_IN_SINE
        if str == 'ease_out_sine': return TweenEaseType.EASE_OUT_SINE
        if str == 'ease_in_out_sine': return TweenEaseType.EASE_IN_OUT_SINE
        if str == 'ease_in_quad': return TweenEaseType.EASE_IN_QUAD
        if str == 'ease_out_quad': return TweenEaseType.EASE_OUT_QUAD
        if str == 'ease_in_out_quad': return TweenEaseType.EASE_IN_OUT_QUAD
        if str == 'ease_in_cubic': return TweenEaseType.EASE_IN_CUBIC
        if str == 'ease_out_cubic': return TweenEaseType.EASE_OUT_CUBIC
        if str == 'ease_in_out_cubic': return TweenEaseType.EASE_IN_OUT_CUBIC
        if str == 'ease_in_quart': return TweenEaseType.EASE_IN_QUART
        if str == 'ease_out_quart': return TweenEaseType.EASE_OUT_QUART
        if str == 'ease_in_out_quart': return TweenEaseType.EASE_IN_OUT_QUART
        if str == 'ease_in_quint': return TweenEaseType.EASE_IN_QUINT
        if str == 'ease_out_quint': return TweenEaseType.EASE_OUT_QUINT
        if str == 'ease_in_out_quint': return TweenEaseType.EASE_IN_OUT_QUINT
        return TweenEaseType.EASE_COSINE
